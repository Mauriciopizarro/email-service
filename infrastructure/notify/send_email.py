import ssl
from config import settings
import smtplib
from email.message import EmailMessage
from domain.interfaces.notify_users import NotifyUser
from infrastructure.notify.templates.register_mail import get_body_mail_new_register
from infrastructure.notify.templates.register_mail_v2 import get_body
from infrastructure.notify.templates.reset_password_email import get_body_mail_reset_pass
from infrastructure.notify.templates.code_verification_email import get_body_mail_verification_code


class SendEmail(NotifyUser):

    def __init__(self):
        self.email_sender = settings.EMAIL
        self.email_password = settings.EMAIL_PASSWORD

    def send_email(self, user_email, subject, body):
        mail = EmailMessage()
        mail["From"] = self.email_sender
        mail["To"] = user_email
        mail["Subject"] = subject
        mail.set_content(body, subtype='html')
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(settings.EMAIL_HOST, port=settings.EMAIL_PORT, context=context) as smtp:
            smtp.login(self.email_sender, self.email_password)
            smtp.sendmail(self.email_sender, user_email, mail.as_string())

    @staticmethod
    def get_password_updated_mail(username):
        return get_body_mail_reset_pass(username)

    @staticmethod
    def get_user_created_mail(username):
        return get_body(username)

    @staticmethod
    def get_validation_code_send_email(code):
        return get_body_mail_verification_code(code)
