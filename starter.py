from infrastructure.events.listeners.reset_password_code_verification_email import ResetPassVerificationCodelListener
from infrastructure.events.listeners.reset_pass_send_email import PassResetSendEmailListener
from infrastructure.events.listeners.user_created_send_email import UserCreatedSendEmailListener
from threading import Thread
import time

def start():
    time.sleep(10)
    Thread(target=UserCreatedSendEmailListener).start()
    Thread(target=ResetPassVerificationCodelListener).start()
    Thread(target=PassResetSendEmailListener).start()



if __name__ == "__main__":
    start()