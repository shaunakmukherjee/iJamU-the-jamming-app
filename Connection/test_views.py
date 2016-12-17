#Connection/test_views

from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User,AnonymousUser
from .views import Requests

class Test_Connection(TestCase):
    fixtures = ['user_data','userdetail_data','crequest_data','connection_data']
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
    
    def test_requests(self):
        response = self.c.post('/requests/')
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'requests/req.html')
        self.assertEquals(response.context['userdetail'][0].__str__(),'test2')
        self.assertEquals(response.context['userdetail'][1].__str__(),'test3')
    
    #def test_reqsearch(self):
    #    response = self.c.post('/requests/',{'key':'2'},'/')
    #    self.assertEquals(response.status_code,200)
    #    self.assertTemplateUsed(response,'requests/reqlist.html')
    #    self.assertEquals(response.context['userdetail'][0].__str__(),'test2')
    
    def test_connections(self):
        response = self.c.post('/connections/')
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'connections/con.html')
        self.assertEquals(response.context['userdetail'][0].__str__(),'test3')
    
    def test_messaging(self):
        response = self.c.post('/messaging/')
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'messaging.html')