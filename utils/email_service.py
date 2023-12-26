from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from smtplib import SMTPException


class EmailSender:
    def __init__(self, subject, to, context, template_name):
        self.subject = subject
        self.to = to
        self.context = context
        self.template_name = template_name

    def send(self):
        try:
            html_message = render_to_string(self.template_name, self.context)
            plain_message = strip_tags(html_message)
            from_email = settings.EMAIL_HOST_USER
            send_mail(self.subject, plain_message, from_email, [self.to], html_message=html_message)
        except SMTPException as e:
            print(f'SMTP error while sending email: {e}')

    def reset(self):
        self.subject = None
        self.to = None
        self.context = None
        self.template_name = None
