import time
from celery import shared_task

#task for celery worker


def send_email(email_id):
    print("Sending email...")
    time.sleep(10)
    print(f"Email sent to {email_id} with appointment details.")
