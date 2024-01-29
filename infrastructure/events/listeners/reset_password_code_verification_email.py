import json
from infrastructure.notify.send_email import SendEmail
from infrastructure.events.rabbit_consumer import RabbitConsumer


class ResetPassVerificationCodelListener(RabbitConsumer):
    topic = "send_reset_password_code_email"

    def process_message(self, channel, method, properties, body):
        event = json.loads(body)
        mail = SendEmail()
        mail.send_email(user_email=event["email"],
                        subject=event["subject"],
                        body=mail.get_validation_code_send_email(event["validation_code"]))
