from infrastructure.events.consumers.reset_pass_send_email import PassResetSendEmailListener
from infrastructure.events.consumers.user_created_send_email import UserCreatedSendEmailListener
from threading import Thread


def start():
    # We configure consumers

    #password_updated_send_email
    Thread(target=PassResetSendEmailListener).start()
    #user_created_send_email
    Thread(target=UserCreatedSendEmailListener).start()


if __name__ == "__main__":
    start()
