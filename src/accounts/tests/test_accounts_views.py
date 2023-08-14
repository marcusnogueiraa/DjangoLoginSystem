from .test_accounts_base import AccountsTestBase
from django.urls import reverse, resolve
from accounts import views


class AccountsViewsTest(AccountsTestBase):


    def test_accounts_login_view_function_is_correct(self):
        view = resolve(reverse('accounts:login_view'))
        self.assertIs(view.func, views.login_view)

    def test_accounts_register_view_function_is_correct(self):
        view = resolve(reverse('accounts:register_view'))
        self.assertIs(view.func, views.register_view)

    def test_accounts_login_view_returns_status_code_200_OK(self):
        login_view_url = reverse('accounts:login_view')
        response = self.client.get(login_view_url)
        self.assertEqual(response.status_code, 200)

    def test_accounts_register_view_returns_status_code_200_OK(self):
        register_view_url = reverse('accounts:register_view')
        response = self.client.get(register_view_url)
        self.assertEqual(response.status_code, 200)

    def test_accounts_login_view_loads_correct_template(self):
        login_view_url = reverse('accounts:login_view')
        response = self.client.get(login_view_url)
        self.assertTemplateUsed(response, 'accounts/pages/login.html')

    def test_accounts_register_view_loads_correct_template(self):
        register_view_url = reverse('accounts:register_view')
        response = self.client.get(register_view_url)
        self.assertTemplateUsed(response, 'accounts/pages/register.html')

