from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.crypto import get_random_string
from django.utils.html import strip_tags

UserModel = get_user_model()


# Signal handler to send an email to a newly created user
@receiver(signal=post_save, sender=UserModel)
def send_email(instance, created, **kwargs):
    # Check if the instance (user) is newly created
    if not created:
        return

    # Generate a 4-digit verification code using Django's get_random_string function
    verification_code = get_random_string(length=4, allowed_chars='0123456789')
    # Create the email content using a template (email-greeting.html) and passing the username and code
    email_content = render_to_string('email-greeting.html', {
            'username': instance.username, 'code': verification_code})

    # Send the email to the user using Django's send_mail function
    send_mail(
        subject="Welcome to PassKeeper",
        message=strip_tags(email_content),
        html_message=email_content,
        from_email='info.passkeeper@gmail.com',
        recipient_list=(instance.email,)
    )

    # Hash the verification_code and store it in the user's access_code field
    instance.access_code = make_password(verification_code)
    instance.save()
