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
