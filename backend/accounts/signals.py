import random
import string

from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save


User = get_user_model()

# Handles the username empty check


@receiver(pre_save, sender=User)
def fill_username_for_user(sender, instance, *args, **kwargs):
    if not instance.username:
        # Generate a unique random 8 chracter username check if it is unique
        while True:
            username = "".join(
                random.choice(string.ascii_lowercase + string.digits) for _ in range(8)
            )
            if not User.objects.filter(username=username).exists():
                instance.username = username
                break
