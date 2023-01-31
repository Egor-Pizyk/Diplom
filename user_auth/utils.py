from django.conf import settings
from django.core.mail import send_mail


def send_email(email, code):
    subject = 'Відновлення паролю'
    message = f'Перейдіть за посиланням та введіть новий пароль\nhttp://127.0.0.1:8000/remind/{code.decode()}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email, ]
    send_mail(subject, message, email_from, recipient_list)