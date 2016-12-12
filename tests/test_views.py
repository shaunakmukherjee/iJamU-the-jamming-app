# Enables use of dummy web browser
from django.test import Testcase, Client
from django.contrib.auth.models import User

# imports of views
from /Login import views

# test views validations with HTTP
class Test_Validations(TestCase):
    fixtures = ['user','user_detail']

    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user(username='test', password='12345')
    
    # LOGIN home()
    def test_login(self):
        # login using test user
        response = self.c.post('login/',{'username': 'test', 'password': '12345'})
        
        # test for login failures
        
        # find actual response code
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.templates, 'home.html')
        
    #REGISTER register()
    def test_register():
        # open the register page
        response = self.c.post('/accounts/register/', follow=true)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.templates, 'registration/registration_form.html')
        
        # Complete registration
        # Consider making a test fixture
        response = self.c.post('/accounts/register/',{'Fname':'John',
                               'Lname':'Doe','Techlevel':'1','Year':'1','Rating':'1',
                               'Bio':'test is life','Instruments':'Guitar',
                               'Genre':'Rock'},follow=true)
                
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.redirectchain,[('http://testserver/accounts/register/complete',302),
                                                 ('post_detail'),302])
        self.assertEqual(response.templates, 'profilesearch/profile.html')
        
        
        
    