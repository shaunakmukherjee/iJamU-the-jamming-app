from django.test import TestCase
# imports for testing the model
from .models import Userdetails,Search
# imports for testing the view
#from . import views
#import unittest
# imports for testing the form
#from .forms import PostForm, SearchForm

# models test

# test the Userdetails model
class UserdetailTest(TestCase):
    
    # creates a test user
    def create_user(self, Username = "test1",
                          Fname = "John",
                          Lname = "Doe",
                          Nickname = "JD",
                          Techlevel = "3",
                          Year = "2",
                          Rating = "4",
                          Bio = "Test is life",
                          Genre = "Rock",
                          Address = "1 E UNIV PKWY, Unit 906, Baltimore, MD, 21218"
                          Instruments = "Guitar"):
        return Userdetails.objects.create(Username = Username,
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
        u = self.create_user()
        self.assertTrue(isinstance(u, Userdetails))
        self.assertEqual(u.__str__(), u.Username)
        
# test the Search model
class SearchTest(TestCase):
    
    # creates a test search
    def create_search(self, Criteria = "Guitar"):
        return Search.objects.create(Criteria = Criteria)
    
    # tests whether the search was created and checks the __str__ method
    def test_search_creation(self):
        s = self.create_search()
        self.assertTrue(isinstance(s, Search))
        self.assertEqual(s.__str__(), s.Instruments)

# test the Connections model
#class ConnectionsTest(TestCase):
#    
#    # creates a test connection
#    def create_connections(self, User1 = "John Doe",
#                                 User2 = "Jane Doe"):
#        return Connections.objects.create(User1 = User1,
#                                          User2 = User2)
#    
#    # tests whether the connection was created and checks the __str__ method
#    def test_connection_creation(self):
#        c = self.create_connections()
#        self.assertTrue(isinstance(c, Connections))
#        self.assertEqual(c.__str__(), s.User1)

# test the view

#class TestSignup(unittest.TestCase):
#    def setUp(self):
#    def test_signup_success(self):
#    # there are more than one failures
#    def test_signup_failure(self):
#
#class TestLogin(unittest.TestCase):
#
#class TestSearch(unittest.TestCase):
#
#class TestEndorse(unittest.TestCase):
#
#if __name__ = '__main__':
#    unittest.main

# need to add more test after framework on views is complete

# test the forms

# need to add testing for api