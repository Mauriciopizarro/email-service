import json
from infrastructure.events.rabbit_consumer import RabbitConsumer
from infrastructure.notify.send_email import SendEmail


class UserCreatedSendEmailListener(RabbitConsumer):
    topic = "user_created_send_email"

    def process_message(self, channel, method, properties, body):
        event = json.loads(body)
        mail = SendEmail()
        message = mail.get_user_created_mail(event["username"])
        mail.send_email(user_email=event["email"], subject=event["subject"], body=message)
