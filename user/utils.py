from django.core.mail import EmailMessage
import os


class Utils:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['subject'],
            body=data['body'],
            from_email=os.getenv('EMAIL_HOST_USER'),
            to=[data['to_email']]
        )
        email.send()
