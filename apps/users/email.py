import random
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _

from apps.users.models import User


def send_email_confirmation(email):
    code = random.randint(1000, 9999)
    subject = _("Email Confirmation")
    message = _(
        f"Hello! Your email address was provided for logging into the Oracle application. "
        f"Please enter this code on the login page: {code}. "
        f"If this was not you or you did not register on the site, simply ignore this email."
    )
    email_from = "ttestdb01@gmail.com"
    send_mail(subject, message, email_from, [email])
    user_obj = User.objects.get(email=email)
    user_obj.otp = code
    user_obj.save()
