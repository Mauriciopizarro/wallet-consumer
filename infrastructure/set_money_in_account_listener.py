import json
from infrastructure.rabbit_consumer import RabbitConsumer
import requests
from config import settings


class SetMoneyAccountListener(RabbitConsumer):
    topic = "set_money_account"

    def process_message(self, channel, method, properties, body):
        event = json.loads(body)
        user_id = event["user_id"]
        amount = event["amount"]
        url = F"{settings.MONEY_SERVICE_URL}/wallet/set_money"
        requests.post(url=url, json={
            "user_id": user_id,
            "amount": amount
        })
