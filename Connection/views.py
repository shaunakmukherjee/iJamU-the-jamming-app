#Connections/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Connection,Crequest
# import Userdetail models from Profile app
from Profile.models import Userdetail
from django.contrib.auth.models import User,AnonymousUser
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.db.models import Q
from django.shortcuts import render_to_response
from django.core.context_processors import csrf 
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.mail import send_mail

#Displays Requests
def Requests(request):
    # Creates an array Requests sent to the user. 
    if isinstance(request.user,AnonymousUser):
        request.user = User.objects.get(username='test1')
    pseudov=str(request.user)
    userdetail= Crequest.objects.filter(User1=pseudov)
    #Renders the list of pending requests.
    return render(request, 'requests/req.html', {'userdetail':userdetail})

# Displays userdetails of a user with options of accepting or rejecting the request.
def reqsearch(request, **kwargs):
    if isinstance(request.user,AnonymousUser):
        request.user = User.objects.get(username='test1')
     # Get username of the user.
    pseudov=str(request.user)
    for key, value in kwargs.iteritems():
        s=value;
    # Get the users profile. Why do they filter through Userdetail and not Crequest??
    userdetail= Userdetail.objects.filter(Q(Nickname=s)).order_by('Rating')
    # Render Users details.
    return render(request, 'requests/reqlist.html', {'userdetail':userdetail})

# Request to connect.
def makereq(request, **kwargs):
    # Get username of the user.
    pseudov=str(request.user)
    for key, value in kwargs.iteritems():
        s=value;
    # Create the request object in the database.
    k=Crequest(User1=s,User2=pseudov)
    # Store in the database.
    k.save()
    return render(request, 'actions/sent.html')

# Delete the request from the database after the request has been either accepted or declined.
def delreq(request, **kwargs):
     # Get username of the user.
    pseudov=str(request.user)
    for key, value in kwargs.iteritems():
        s=value;  
    # Get the request object from the database  
    k=get_object_or_404(Crequest,User1=pseudov,User2=s)
    # Delete the request
    k.delete()
    return render(request, 'actions/reject.html')

# Create a connection, Adding redundancy to make querying easier.
def accept(request, **kwargs):
    # Get username of the user.
    pseudov=str(request.user)
    for key, value in kwargs.iteritems():
        s=value;
    # Create the connect object in the database.
    k=Connection(User1=s,User2=pseudov)
    # Store in the database.
    k.save()
    # Create the connect object in the database.
    k=Connection(User1=pseudov,User2=s)
    # Store in the database.
    k.save()
    k=get_object_or_404(Crequest,User1=pseudov,User2=s)
    # Delete the request
    k.delete()
    return render(request, 'actions/accept.html')



#CONNECTIONS.

#Displays the connections of the user
def Connections(request):
    # Creates an array of Users connected with the user
    pseudov=str(request.user)
    userdetail= Connection.objects.filter(User1=pseudov)
    # Renders the list of connected users
    return render(request, 'connections/con.html', {'userdetail':userdetail})


# Displays userdetails of a user with option of messaging or deleting the contact.
def consearch(request, **kwargs):
    # Get username of the user.
    pseudov=str(request.user)
    for key, value in kwargs.iteritems():
        s=value;
    # Get the users profile.
    userdetail= Userdetail.objects.filter(Q(Nickname=s)).order_by('Rating')
    # Render Users details.
    return render(request, 'connections/conlist.html', {'userdetail':userdetail})

# Delete the connection from the database.
def deleteconnection(request, **kwargs):
     # Get username of the user.
    pseudov=str(request.user) 
    for key, value in kwargs.iteritems():
        s=value;  
    # Get the request object from the database  
    k=get_object_or_404(Connection,User1=pseudov,User2=s)
    # Delete the connection from the user's end.
    k.delete()
    # Get the request object from the database  
    k=get_object_or_404(Connection,User1=s,User2=pseudov)
    # Delete the connection from the other end.
    k.delete()
    return render(request, 'actions/deleteconnection.html')


#MESSAGING.

#Displays Messaging
def Messaging (request):
    return render(request,'messaging.html')

#For e-mail
def Email(request):
    send_mail('Whatsup!', 'We are connected', 'tplusus@gmail.com', ['shaunak.mukherjee94@gmail.com'])