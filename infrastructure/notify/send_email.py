import ssl
from config import settings
import smtplib
from email.message import EmailMessage
from domain.interfaces.notify_users import NotifyUser
from infrastructure.notify.templates.register_mail import get_body_mail


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
        html = """
                <html>
                  <head>
                    <style>
                      body {{
                        font-family: Arial, sans-serif;
                        font-size: 14px;
                        color: #333;
                      }}
                      h1 {{
                        color: #007bff;
                      }}
                    </style>
                  </head>
                  <body>
                    <h1>Hi {username}</h1>
                    <p>Password updated successfully</p>
                  </body>
                </html>
                """.format(username=username)

        return html

    @staticmethod
    def get_user_created_mail(username):
        return get_body_mail(username)
