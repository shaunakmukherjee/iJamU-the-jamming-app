# Enables use of dummy web browser
from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Userdetail

# imports of views
from . import views

# test Login and Signup
class Test_Login_Signup(TestCase):
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
        self.c.logout()
        # Check if server does not redirect if incorrect login is given
        response = self.c.post('/login/',{'username':'test1','password':'00000'},follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.redirect_chain, [])
        # Check if server correctly redirects of correct login is given
        response = self.c.post('/login/',{'username':'test1','password':'11111'},follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.redirect_chain, [('http://testserver/',302)])
        self.assertTemplateUsed(response,'home.html')

    #REGISTER register()
    def test_register(self):
        # open the register page
        response = self.c.head('/accounts/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'registration/registration_form.html')
        # test for invalid registration. Redirects back to registration form
        response = self.c.post('/accounts/register/',{'username': 'test1',
                               'password1': '00000','password2':'00000'},follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'registration/registration_form.html')
        # Passwords don't match. Redirects to profile edit form
        response = self.c.post('/accounts/register/',{'username': 'newtest',
                               'password1': '00000','password2':'01010'},follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'registration/registration_form.html')
        # Give valid registration information
        response = self.c.post('/accounts/register/',{'username': 'newtest',
                               'password1': '00000','password2':'00000'},follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'profilesearch/post_edit.html')    
    
        
        
        
    