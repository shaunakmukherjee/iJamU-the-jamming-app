from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
# imports for testing the view
from . import views

# test user profile
class TestUserProfile(TestCase):

    def setUp(self):
        self.factory = RequestFacotry()
        self.user = User.objects.create_user(username='usertest', password='12345')
    
    # test profile creation
    def test_create_profile(self):
        
        
    def test_update():