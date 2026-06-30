ImportErrormport json
import os
import requests
from dotenv import load_dotenv
from kafka import KafkaConsumer

load_dotenv()

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')

def send_telegram_msg(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    requests.post(url, json=payload)

def start_listener():
    consumer = KafkaConsumer(
        'partner_events',
        bootstrap_servers=[BOOTSTRAP_SERVERS],
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        group_id='telegram_bot_group'
    )
    
    print("Бот-слушатель запущен и ожидает события...")
    
    for message in consumer:
        event = message.value
        msg = (
            f"🚀 *Событие в БД*\n\n"
            f"Действие: {event.get('event_type')}\n"
            f"Название: {event.get('title')}\n"
            f"Партнер: {event.get('partner')}\n"
            f"Количество: {event.get('count')}"
        )
        send_telegram_msg(msg)
        print(f"Уведомление отправлено: {event.get('title')}")

if __name__ == "__main__":
    start_listener()