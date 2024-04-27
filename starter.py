import time
from threading import Thread
from infrastructure.events.consumers.reset_pass_send_email import PassResetSendEmailListener
from infrastructure.events.consumers.reset_password_code_verification_email import ResetPassVerificationCodelListener
from infrastructure.events.consumers.user_created_send_email import UserCreatedSendEmailListener


def start():
    time.sleep(10)
    Thread(target=UserCreatedSendEmailListener).start()
    Thread(target=ResetPassVerificationCodelListener).start()
    Thread(target=PassResetSendEmailListener).start()


if __name__ == "__main__":
    start()
