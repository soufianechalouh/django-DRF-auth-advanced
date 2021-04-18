from django.core.mail import EmailMessage


class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(data["email_subject"], data["email_body"], from_email="deals.mastery@gmail.com", to=[data["to"]])
        email.send()
