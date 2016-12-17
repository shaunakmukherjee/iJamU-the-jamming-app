from django.test import TestCase
from django.contrib.auth.models import User

# imports for testing the model
from .models import Userdetail,Search

# test the Userdetails model
class UserdetailTest(TestCase):
    
    # creates a test user
    def setUp(self):
        self.user = User.objects.create_user(username='usertest', password='12345')
    
    # creates a test userdetail
    def create_userdetail(self,
                          Fname = "John",
                          Lname = "Doe",
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
                                          Nickname = str(self.user),
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
        self.assertEqual(u.Nickname,str(self.user))

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
