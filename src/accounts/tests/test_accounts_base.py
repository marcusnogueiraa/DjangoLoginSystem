from django.test import TestCase
from accounts.models import CustomUser


class AccountsTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def create_user(self, username="johndoe", password="password", email="johndoe@example.com"):
        return CustomUser.objects.create_user(username=username, email=email, password=password)

