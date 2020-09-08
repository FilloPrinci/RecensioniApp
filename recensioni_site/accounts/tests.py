from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from recensioni_site import settings
from django.contrib.auth.models import User

class testRegistrazione(TestCase):

    def setUp(self):
        self.proprietario1 = User.objects.create(username="Proprietario1", email="proprietario1@gmail.com", password1="PasswordProprietario1", is_staff="True")
        self.proprietario2 = User.objects.create(username="Proprietario2", email="proprietario2@gmail.com", password1="PasswordProprietario2", is_staff="True")
        #--------------------------------------------
        self.user1 = User.objects.create(username="User1", email="user1@gmail.com", password1="PasswordUser1", is_staff="False")
        self.user2 = User.objects.create(username="User2", email="user2@gmail.com", password1="PasswordUser2", is_staff="False")

    def tearDown(self):
        self.proprietario1.delete()
        self.proprietario2.delete()
        # --------------------------------------------
        self.user1.delete()
        self.user2.delete()


