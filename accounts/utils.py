from django.conf import settings

import random
import string
import logging
from uuid import uuid4
from rest_framework_simplejwt.tokens import RefreshToken


logger = logging.getLogger(__name__)


def create_authentication_token(user):
    """Custom way to create an authentication token"""
    return (RefreshToken.for_user(user), True)


def generate_employee_id(n=settings.PROJECT_EMPLOYEE_ID_LENGTH):
    unique_code = (
        str(uuid4())[:n]
        .upper()
        .replace("-", random.choice(string.ascii_uppercase))
        .replace("#", random.choice(string.ascii_uppercase))
        .replace("@", random.choice(string.ascii_uppercase))
    )
    return f"DJ{unique_code}"
