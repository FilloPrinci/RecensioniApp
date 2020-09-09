from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from recensioni_site import settings
from django.contrib.auth.models import User
from forum.models import Sezione,Post,UserDataReccomandation

class testRegistrazione(TestCase):

    def setUp(self):
        self.credential = {'username': 'dummy', 'password': 'dummypassword', 'is_staff': 'False'}

        self.credentialp = {'username':'dummyp', 'password':'dummypasswordp', 'is_staff':'True'}

        self.proprietario1 = User.objects.create(username="Proprietario1",
                                                 email="proprietario1@gmail.com",
                                                 password="PasswordProprietario1",
                                                 is_staff="True")

        self.proprietario2 = User.objects.create(username="Proprietario2",
                                                 email="proprietario2@gmail.com",
                                                 password="PasswordProprietario2",
                                                 is_staff="True")

        #--------------------------------------------

        self.user1 = User.objects.create(username="User1",
                                         email="user1@gmail.com",
                                         password="PasswordUser1",
                                         is_staff="False")

        self.user2 = User.objects.create(username="User2",
                                         email="user2@gmail.com",
                                         password="PasswordUser2",
                                         is_staff="False")

        # --------------------------------------------

        self.sezione1 = Sezione.objects.create(user=self.proprietario1,
                                               nome_sezione="hotel1",
                                               descrizione="descrizione",
                                               citta="città_test",
                                               provincia="provincia_test",
                                               indirizzo="indirizzo_test",
                                               logo_sezione="null",
                                               hotelB="True",
                                               ristoranteB="False",
                                               fastFoodB="False",
                                               casaVacanzaB="False",
                                               agriturismoB="False")

        self.post1 = Post.objects.create(autore_post=self.user1,
                                         contenuto="post_test",
                                         rating=5,
                                         data_creazione=timezone.now(),
                                         sezione=self.sezione1)

        self.post2 = Post.objects.create(autore_post=self.user1,
                                         contenuto="post_test",
                                         rating=3,
                                         data_creazione=timezone.now(),
                                         sezione=self.sezione1)

    def tearDown(self):
        self.proprietario1.delete()
        self.proprietario2.delete()
        # --------------------------------------------
        self.user1.delete()
        self.user2.delete()
        # --------------------------------------------
        self.sezione1.delete()
        self.post1.delete()


    def test_vsualizzaSezione(self):
        self.client.login(**self.credential)
        response= self.client.get('/forum/sezione/' + str(self.sezione1.id) + '/')
        self.assertTemplateUsed(response, 'forum/singola_sezione.html')
        self.assertEqual(response.status_code, 200)

    def test_rating(self):
        self.client.login(**self.credential)
        response = self.client.get('/forum/sezione/' + str(self.sezione1.id) + '/')
        self.assertEqual(response.context['sezione'], self.sezione1)
        self.assertEqual(response.context['media_rating'], 4)
