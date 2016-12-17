#Connection/test_models

from django.test import TestCase
from .models import Connection,Crequest
from django.contrib.auth.models import User

# Create your tests here.
# test the Connection model
class ConnectionTest(TestCase):
    
    # creates 2 test users
    def setUp(self):
        self.user1 = User.objects.create_user(username='usertest1', password='12345')
        self.user2 = User.objects.create_user(username='usertest2', password='54321')
    
    # creates a test connection
    def create_connection(self):
        return Connection.objects.create(User1=self.user1,User2=self.user2)
        
    # tests whether the connection was created and checks the __str__ method
    def test_connection_creation(self):
        c = self.create_connection()
        self.assertTrue(isinstance(c, Connection))
        self.assertEqual(c.__str__(), str(c.User2))
    
    # test the other user and boolean default

# test the connection request model
class CrequestTest(TestCase):
    
    # creates 2 test users
    def setUp(self):
        self.user1 = User.objects.create_user(username='usertest1', password='12345')
        self.user2 = User.objects.create_user(username='usertest2', password='54321')
    
    # creates a connection request
    def create_Crequest(self):
        return Crequest.objects.create(User1=self.user1,User2=self.user2)
        
    # tests whether the request was created and checks the __str__ method
    def test_connection_creation(self):
        cr = self.create_Crequest()
        self.assertTrue(isinstance(cr, Crequest))
        self.assertEqual(cr.__str__(), str(cr.User2))