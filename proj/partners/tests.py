from django.test import TestCase
from unittest.mock import patch, MagicMock
#from proj.partners.models import PartnerOffer, Category
from partners.models import PartnerOffer, Category

class PartnerSignalsTest(TestCase):
    def setUp(self):
        self.cat = Category.objects.create(name="Test")

    @patch('proj.partners.signals.get_producer')
    def test_kafka_event_on_create(self, mock_get_producer):
        # Создаем мок-продюсер
        mock_producer = MagicMock()
        mock_get_producer.return_value = mock_producer
        
        # Создаем объект
        offer = PartnerOffer.objects.create(
            title="Test Offer", 
            category=self.cat,
            count=10
        )
        
        # Проверяем, что send был вызван
        self.assertTrue(mock_producer.send.called)
        args, _ = mock_producer.send.call_args
        self.assertEqual(args[0], 'partner_events')
        self.assertEqual(args[1]['title'], "Test Offer")