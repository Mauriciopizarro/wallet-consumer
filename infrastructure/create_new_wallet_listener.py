import json
from infrastructure.rabbit_consumer import RabbitConsumer
import requests
from config import settings


class CreateNewWalletListener(RabbitConsumer):
    topic = "create_new_wallet"

    def process_message(self, channel, method, properties, body):
        event = json.loads(body)
        user_id = event["user_id"]
        url = f"{settings.MONEY_SERVICE_URL}/wallet/create_wallet/{user_id}"
        requests.post(url=url)
