from unittest import skip
from .test_accounts_base import AccountsTestBase
from django.urls import reverse, resolve
from accounts import views
from accounts.models import CustomUser
from django.db import IntegrityError


class AccountsAuthenticationTest(AccountsTestBase):


    def test_authenticated_user_can_access_sucess_page(self):
        user_username, user_password = 'johndoe', 'password'
        self.create_user(username=user_username, password=user_password)
        self.client.login(username=user_username, password=user_password)

        sucess_page_url = reverse('accounts:sucess_view')
        response = self.client.get(sucess_page_url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('GO TO MAIN PAGE', response.content.decode())

    @skip('Work In Progress')
    def test_unauthenticated_user_cannot_access_sucess_page(self):
        sucess_page_url = resolve(reverse('accounts:sucess_view'))
        response = self.client.get(sucess_page_url)
        self.assertRedirects(response.url, '/login/?next=/sucess/', status_code=302)

    def test_if_is_possible_register_a_user(self):
        expected_username = 'johndoe'
        user_register_url = reverse('accounts:user_register')
        self.client.post(user_register_url, {'username':expected_username, 'password':'password', 'email':'johndoe@gmail.com'})

        user = CustomUser.objects.filter(username=expected_username).first()
        self.assertIsNotNone(user)

    def test_if_is_not_possible_register_two_users_with_same_username(self):
        user_username = 'johndoe'
        self.create_user(username=user_username, password='password1', email='johndoe1@gmail.com')
        user_register_url = reverse('accounts:user_register')
        with self.assertRaises(IntegrityError):
            self.client.post(user_register_url, {'username':user_username,
                                                 'password':'password2', 'email':'johndoe2@gmail.com'})

    def test_if_is_not_possible_register_two_users_with_same_email(self):
        user_email = 'johndoe@example.com'
        self.create_user(username='johndoe1', password='password1', email=user_email)
        user_register_url = reverse('accounts:user_register')
        with self.assertRaises(IntegrityError):
            self.client.post(user_register_url, {'username':'johndoe2', 'password':'password2', 'email':user_email})

    def test_if_its_possible_to_login_into_an_existing_account(self):
        expected_username, expected_password = 'johndoe', 'password'
        self.create_user(username=expected_username, password=expected_password, email='johndoe@example.com')

        user_login_url = reverse('accounts:user_login')
        response = self.client.post(user_login_url, {'username':expected_username, 'password':expected_password})
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_if_is_not_ipossible_login_into_an_unexisting_account(self):
        user_login_url = reverse('accounts:user_login')
        response = self.client.post(user_login_url, {'username':'johndoe', 'password':'password'})
        self.assertFalse(response.wsgi_request.user.is_authenticated)




