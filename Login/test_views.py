# Enables use of dummy web browser
from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Userdetail

# imports of views
from . import views

# test Login and Signup
class Test_Validations(TestCase):
    # Install the test fixtures for user and userdetail
    fixtures = ['user_data','userdetail_data']
    usrs = User.objects.all()

    def setUp(self):
        self.c = Client()
        
        # set/hash the passwords of the users
        for u in self.usrs:
            u.set_password(u.password)
            u.save()
    
    # LOGIN home()
    def test_login(self):
        # test for login failures
        logged = self.c.login(username='falsetest',password='00000');
        self.assertEqual(logged,False)
        # test for incorrect password
        logged = self.c.login(username='test1',password='00000');
        self.assertEqual(logged,False)
        # login using test user
        logged = self.c.login(username='test1',password='11111');
        self.assertEqual(logged,True)

    #REGISTER register()
    def test_register(self):
        # open the register page
        response = self.c.head('/accounts/register/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.templates, 'registration/registration_form.html')
        
        # Complete registration
        response = self.c.post('/accounts/register/',{'username': 'newtest',
                               'password': '55555'},follow=True)
        # test for invalid registration
                
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(response.redirectchain,[('http://testserver/accounts/register/complete',302),
        #                                         ('post_detail',304)])
        #self.assertEqual(response.templates, 'profilesearch/post_edit.html')
    
    
        
        
        
    