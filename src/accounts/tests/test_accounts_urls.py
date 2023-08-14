from .test_accounts_base import AccountsTestBase
from django.urls import reverse, resolve
from accounts import views


class AccountsURLsTest(AccountsTestBase):


    def test_accounts_login_view_url_is_correct(self):
        url = reverse('accounts:login_view')
        self.assertEqual(url, '/login/')

    def test_accounts_register_view_url_is_correct(self):
        url = reverse('accounts:register_view')
        self.assertEqual(url, '/register/')

    def test_accounts_sucess_view_url_is_correct(self):
        url = reverse('accounts:sucess_view')
        self.assertEqual(url, '/sucess/')



