import json
from infrastructure.notify.send_email import SendEmail
from infrastructure.events.rabbit_consumer import RabbitConsumer


class PassResetSendEmailListener(RabbitConsumer):
    topic = "password_updated_send_email"

    def process_message(self, channel, method, properties, body):
        event = json.loads(body)
        mail = SendEmail()
        mail.send_email(user_email=event["email"], subject=event["subject"], body=mail.get_password_updated_mail(event["username"]))
