from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import IntegrityError


User = get_user_model()


class UsersManagersTests(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(mobile="+918888888888", password="pwd")
        self.assertEqual(user.mobile_number, "+918888888888")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(mobile="")

    def test_user_without_password(self):
        user = User.objects.create_user(
            full_name="Foo", mobile="+919873543210", password=""
        )
        self.assertFalse(user.has_usable_password())
        self.assertFalse(user.check_password(None))

    def test_email_uniqueness(self):
        u1 = User.objects.create_user(
            mobile="+918888888888", password="", email="gaurav@email.com"
        )
        u2 = User.objects.create_user(
            mobile="+919999999999", password="", email="gaurav@email.com"
        )
        with self.assertRaises(ValidationError):
            u1.full_clean()
            u2.full_clean()

    def test_create_superuser(self):
        admin_user = User.objects.create_superuser(username="gaurav", password="pwd")
        self.assertEqual(admin_user.username, "gaurav")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                username="gaurav1", password="pwd", is_superuser=False
            )
