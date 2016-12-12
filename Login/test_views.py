# Enables use of dummy web browser
from django.test import TestCase, Client
from django.contrib.auth.models import User

# imports of views
from . import views

# test views validations with HTTP
class Test_Validations(TestCase):
    fixtures = ['user_fixture','userdetail_fixture']

    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user(username='test', password='12345')
    
    # LOGIN home()
    def test_login(self):
        # login using test user
        response = self.c.post('/login/',{'username': 'test', 'password': '12345'},follow=True)
        
        # test for login failures
        
        # find actual response code
        #self.assertEqual(response.redirectchain,[('http://testserver/login/home.html',302)])
        
    #REGISTER register()
    def test_register(self):
        # open the register page
        response = self.c.head('/accounts/register/')
        
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(response.templates, 'registration/registration_form.html')
        
        # Complete registration
        response = self.c.post('/accounts/register/',{'username': 'newtest',
                               'password': '55555'},follow=True)
        # test for invalid registration
                
        self.assertEqual(response.status_code, 200)
        
        #self.assertEqual(response.redirectchain,[('http://testserver/accounts/register/complete',302),
        #                                         ('post_detail',304)])
        #self.assertEqual(response.templates, 'profilesearch/post_edit.html')
    
    
        
        
        
    