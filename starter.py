from infrastructure.events.consumers.reset_pass_send_email import PassResetSendEmailListener
from infrastructure.events.consumers.user_created_send_email import UserCreatedSendEmailListener
from threading import Thread


def start():
    time.sleep(10)
    Thread(target=UserCreatedSendEmailListener).start()
    Thread(target=ResetPassVerificationCodelListener).start()
    Thread(target=PassResetSendEmailListener).start()


if __name__ == "__main__":
    start()
