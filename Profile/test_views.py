#Profile/test_views.py

# Enables use of dummy web browser
from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User,AnonymousUser
from .models import Userdetail
from .views import post_update,post_detail


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
    
    def test_usrlist(self):
        response = self.c.post('/post/new/')
        self.assertEqual(response.status_code, 200)
        # returns list in order of rating
        self.assertTemplateUsed(response,'profilesearch/post_list.html')
        self.assertEqual(response.context['userdetail'][0].__str__(),'test1')
        self.assertEqual(response.context['userdetail'][1].__str__(),'test2')
        self.assertEqual(response.context['userdetail'][2].__str__(),'test3')        
       
    #def test_profile_creation(self):
        #response = self.c.post('/add/',{'Fname':'Greg',
        #                       'Lname':'House','Year':15, 'Bio':'Everbody Lies',
        #                       'Genre':'Jazz','Address':'Princeton,NJ',
        #                       'Instruments':'Piano'},follow=True)
        #self.assertEqual(response.status_code, 200)
        #self.assertTemplateUsed(response,'profilesearch/post_detail.html')
        #self.assertEqual(response.context['post'][0].__str__(),'newtest')
        #invalid
        
    def test_update_profile(self):
        # open profile edit page update directly if nickname = user
        request = self.f.post('/edit/',{"Username":1,
                "Fname":"John",
                "Lname":"Doe",
                "Nickname":"1",
                "Techlevel":"1",
                "Year":"1",
                "Rating":"1",
                "Bio":"Test Success!",
                "Address":"1 st pkwy",
                "Instruments":"Guitar",
                "Genre":"Rock"})
        request.user = User.objects.get(username='test1')
        response = post_update(request)
        self.assertEqual(response.status_code, 302)
        udtest = Userdetail.objects.get(Nickname=str(request.user))
        self.assertEqual(udtest.Bio,'Test Success!')
    
    def test_get_profile(self):
        response = self.c.post('/connect/',{'pk':1})
        #self.assertEqual(response.status_code, 200)
        #invalid
       
    def test_get_main_profile(self):
        response = self.c.post('/profile/',{'pk':1})
        #self.assertEqual(response.status_code, 200)
        #self.assertEqual(response.context['post'].__str__(),'test1')
        #self.assertTemplateUsed(response,'profilesearch/profile.html')
        #invalid
    
    def test_search(self):
        # open the search page
        response = self.c.head('/post/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'profilesearch/search.html')
        # search for guitar players (test1,test3)
        response = self.c.post('/post/',{'Criteria':'Guitar'},follow=True)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'profilesearch/post_list.html')
        self.assertEqual(response.context['userdetail'][0].__str__(),'test3')
        self.assertEqual(response.context['userdetail'][1].__str__(),'test1')
        # search for violin players (test2)
        response = self.c.post('/post/',{'Criteria':'Violin'},follow=True)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'profilesearch/post_list.html')
        self.assertEqual(response.context['userdetail'][0].__str__(),'test4')
        # search for drum players ()
        response = self.c.post('/post/',{'Criteria':'Drums'},follow=True)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'profilesearch/post_list.html')
        self.assertEqual(response.context['userdetail'].__str__(),'[]')       