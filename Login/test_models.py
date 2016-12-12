from django.test import TestCase
from django.contrib.auth.models import User

# imports for testing the model
from .models import Userdetail,Search,Crequest,Connection

# test the Userdetails model
class UserdetailTest(TestCase):
    
    # creates a test user
    def setUp(self):
        self.user = User.objects.create_user(username='usertest', password='12345')
    
    # creates a test userdetail
    def create_userdetail(self,
                          Fname = "John",
                          Lname = "Doe",
                          Nickname = "JD",
                          Techlevel = "3",
                          Year = "2",
                          Rating = "4",
                          Bio = "Test is life",
                          Genre = "Rock",
                          Address = "1 E UNIV PKWY, Unit 906, Baltimore, MD, 21218",
                          Instruments = "Guitar"):
        return Userdetail.objects.create(Username = self.user,
                                          Fname = Fname,
                                          Lname = Lname,
                                          Nickname = Nickname,
                                          Techlevel = Techlevel,
                                          Year = Year,
                                          Rating = Rating,
                                          Bio = Bio,
                                          Genre = Genre,
                                          Address = Address,
                                          Instruments = Instruments)
    
    # tests whether the user was created and checks the __str__ method
    def test_user_creation(self):
        u = self.create_userdetail()
        self.assertTrue(isinstance(u, Userdetail))
        self.assertEqual(u.__str__(), str(u.Username))
    
    # test the other users
    
# test the Search model
class SearchTest(TestCase):
    
    # creates a test search
    def create_search(self, Criteria = "Guitar"):
        return Search.objects.create(Criteria = Criteria)
    
    # tests whether the search was created and checks the __str__ method
    def test_search_creation(self):
        s = self.create_search()
        self.assertTrue(isinstance(s, Search))
        self.assertEqual(s.__str__(), s.Criteria)

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
        self.assertEqual(c.__str__(), str(c.User1))
    
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
        self.assertEqual(cr.__str__(), str(cr.User1))
    
    # test the other user and boolean default