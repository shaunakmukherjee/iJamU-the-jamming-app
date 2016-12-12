# Enables use of dummy web browser
from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User,AnonymousUser
from .models import Userdetail

# imports of views
from .views import post_detail,post_update,post_new,post_update,usr_list,profile
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
        # MISSING redirect to registration_complete.html  

# Test profile functions
class Test_Profile(TestCase):
    fixtures = ['user_data','userdetail_data']
    usrs = User.objects.all()
    
    def setUp(self):
        self.f = RequestFactory()
        self.c = Client()
        # set/hash the passwords of the users
        for u in self.usrs:
            u.set_password(u.password)
            u.save()

        self.u1 = User.objects.create_user(username='newtest',password='00000')
        self.u1.save()
        
        self.c.user = self.u1
    
    def set_u1_ud(self):
        user1 = self.u1
        return Userdetail.objects.create(Username=user1,Fname='Greg',Lname='House',Techlevel='5',
                                          Year='15',Rating='1',Bio='Everbody Lies',
                                          Instruments='Piano',Genre='Jazz',Nickname='newtest')
        
    
    #def test_get_profile(self):
        #response = self.c.post('/connect/',{'pk':'1'})
        #self.assertEqual(response.status_code, 200)
        #self.assertEqual(response.context.json()['post'].__str__(),str(self.u1))
        #self.assertTemplateUsed(response,'profilesearch/post_details.html')
        # if the given primary key is invalid, return 404
        #response = self.f.post('/connect/?pk=-1')
        #self.assertEqual(response.status_code,404)
    
    def test_usrlist(self):
        response = self.c.post('/post/new/')
        self.assertEqual(response.status_code, 200)
        # returns list in order of rating
        self.assertTemplateUsed(response,'profilesearch/post_list.html')
        self.assertEqual(response.context['userdetail'][0].__str__(),'test1')
        self.assertEqual(response.context['userdetail'][1].__str__(),'test2')
        self.assertEqual(response.context['userdetail'][2].__str__(),'test3')        
    
    #FIX    
    #def test_profile_creation(self):
    #    # redirects to post_detail method if nickname = username
    #    response = self.c.post('/add/',{'Fname':'Greg','Lname':'House', 'Techlevel':'5',
    #                                  'Year':'15','Rating':'1','Bio':'Everbody Lies',
    #                                  'Instruments':'Piano','Genre':'Jazz','Nickname':'Dr.House'})
    #    self.assertEqual(response.status_code, 200)
    #    self.assertTemplateUsed(response,'profilesearch/post_edit.html')
    #    # redirects to post_detail method if nickname = username
    #    request = self.f.post('/add/',{'Fname':'Greg','Lname':'House', 'Techlevel':'5',
    #                                  'Year':'15','Rating':'1','Bio':'Everbody Lies',
    #                                  'Instruments':'Piano','Genre':'Jazz','Nickname':'newtest'})
    #    response = views.post_new(request)
    #    self.assertEqual(response.status_code, 200)
    #    self.assertTemplateUsed(response,'profilesearch/post_details.html')
    #    self.assertEqual(response.context['post'].__str__,str(self.u1))
    #    self.assertEqual(response.context['post'].json()['Lname'],'House')
    
    #FIX
    #def test_update_profile(self):
        # open profile edit page update directly if nickname = user
    #    response = self.c.post('/edit/',{'Fname':'Greg','Lname':'House', 'Techlevel':'5',
    #                                  'Year':'15','Rating':'1','Bio':'Everbody Lies',
    #                                  'Instruments':'Electric Guitar','Genre':'Jazz','Nickname':'Dr.House'})
    #    self.assertEqual(response.status_code, 200)
    #    self.assertTemplateUsed(response,'profilesearch/post_edit.html') 
        # redirects to post_detail method if nickname = username
    #    response = self.c.post('/edit/',{'Fname':'Greg','Lname':'House', 'Techlevel':'5',
    #                                  'Year':'15','Rating':'1','Bio':'Everbody Lies',
    #                                  'Instruments':'Piano','Genre':'Jazz','Nickname':'newtest'})
    #    self.assertEqual(response.status_code, 200)
    #    self.assertTemplateUsed(response,'profilesearch/post_details.html')
    #    self.assertEqual(response.context['post'].__str__,str(self.u1))
    #    self.assertEqual(response.context['post'].json()['Lname'],'House')
    
    def test_get_main_profile(self):
        request = self.f.post('/profile/')
        request.user = self.u1
        ud = self.set_u1_ud()
        ud.save()
        response = views.profile(request,self.u1.pk)
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(response.content.__str__(),str(self.u1))
        #self.assertTemplateUsed(response,'profilesearch/profile.html')