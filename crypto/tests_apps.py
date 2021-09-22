from django.apps import apps
from django.test import TestCase,SimpleTestCase
from .apps import CryptoConfig
from django.contrib.auth import get_user_model
from django.urls import reverse,resolve
from crypto.views import index
from django.conf import settings

class test_AppConfig(TestCase):
    # test app
    def test_app(self):
        self.assertEqual("crypto", CryptoConfig.name)
        self.assertEqual("crypto", apps.get_app_config("crypto").name)

    def test_wrong_secret_key(self):
        SECRET_KEY =settings.SECRET_KEY
        self.assertNotEqual(SECRET_KEY,'wrongkeys')

class CustomUserTests(TestCase):
    # test super user creation
    def test_create_superuser(self):
        User = get_user_model()
        admin = User.objects.create_superuser(
        username='admin',
        email='admin@email.com',
        password='superman'
        )
        self.assertEqual(admin.username, 'admin')
        self.assertEqual(admin.email, 'admin@email.com')
        self.assertTrue(admin.is_active)
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)

class PagesTest(SimpleTestCase):
    def setUp(self):
        url = reverse('index')
        self.response = self.client.get(url)

    def test_index_status(self):
        self.assertEqual(self.response.status_code, 200)

    def test_index_url(self):
        self.assertEqual(self.response.status_code, 200)

    def test_index_template(self):
        self.assertTemplateUsed(self.response, 'index.html')

    def test_index_does_incorrect_template(self):
        self.assertNotContains(self.response,'wrong template')

    def test_index_url_resolve(self):
        view = resolve('/')
        self.assertEqual(
        view.func.__name__,
        index.__name__
        )

    
