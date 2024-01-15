from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User
# Create your tests here.


#AUTOMATIZAMOS UNA COMPROBACION A TRAVEZ DE UNA PRUEBA (EN ESTE CASO SI SE CREA UN PERFIL AUTOMATICAMENTE CUANDO SE CREA UN USUARIO, asi no tenemos que ir a la terminal)
class ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('test', 'test@test.com', 'test1234')
    
    #puede tener el nombre que quiera mientras tenga el "test_" al principio
    def test_profile_exists(self):
        exists = Profile.objects.filter(user__username="test").exists()
        self.assertEqual(exists, True)
    
