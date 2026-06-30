import json
import os
from django.db.models.signals import post_save
from django.dispatch import receiver
#from .models import PartnerOffer
from partners.models import PartnerOffer
from kafka import KafkaProducer
from dotenv import load_dotenv

load_dotenv()

# Инициализируем продюсера как None
_producer = None

def get_producer():
    global _producer
    if _producer is None:
        try:
            _producer = KafkaProducer(
                bootstrap_servers=[os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')],
                value_serializer=lambda v: json.dumps(v, default=str).encode('utf-8')
            )
        except Exception as e:
            print(f"Kafka connection error: {e}")
            return None
    return _producer

@receiver(post_save, sender=PartnerOffer)
def send_offer_to_kafka(sender, instance, created, **kwargs):
    producer = get_producer()
    if producer:
        data = {
            "event_type": "created" if created else "updated",
            "offer_id": instance.id,
            "title": instance.title,
            "partner": instance.partner_name,
            "count": instance.count,
            "link": instance.link
        }
        producer.send('partner_events', data)