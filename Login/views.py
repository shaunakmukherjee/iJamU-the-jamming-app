#Login/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Userdetail,Connection,Crequest
from django.shortcuts import get_object_or_404
from .forms import SearchForm,PostForm
from django.shortcuts import redirect
from django.db.models import Q
from django.shortcuts import render_to_response
from django.core.context_processors import csrf 
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.core.mail import send_mail



#pseudov will be replaced by the session variable of the username.

#MAIN VIEWS.


#LOGIN.
@login_required(login_url="login/")
def home(request):
	return render(request,"home.html")


#REGISTER.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register/complete')

    else:
        form = UserCreationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('registration/registration_form.html', token)

def registration_complete(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(request.POST)
    return render(request, 'profilesearch/post_edit.html', {'form': form})


# Update user details.
def post_update(request):
    if request.method == "POST":
    	pseudov=str(request.user)
        k=Userdetail.objects.get(Nickname=pseudov)
        form = PostForm(request.POST or None,instance = k)
        if form.is_valid():
            post = form.save(commit=True)
            post.username=request.user
            post.Nickname=str(post.Username)
            post.save()
            return redirect('profile', pk=post.pk)
    else:
        form = PostForm(request.POST)
    return render(request, 'profilesearch/post_edit.html', {'form': form})

# Create profile.
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.username=request.user
            post.Nickname=str(post.Username)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(request.POST)
    return render(request, 'profilesearch/post_edit.html', {'form': form})


# Returns the details of a particular user.
def post_detail(request, pk):
    post = get_object_or_404(Userdetail, pk=pk)
    return render(request, 'profilesearch/post_details.html', {'post': post})


#Displays the main profile with all details.
def profile(request, pk):
    post = get_object_or_404(Userdetail, pk=pk)
    return render(request, 'profilesearch/profile.html', {'post': post})


# Returns the list of all users with a few details and links to their profiles.
def usr_list(request):
    userdetail= Userdetail.objects.order_by('Rating')
    return render(request, 'profilesearch/post_list.html', {'userdetail':userdetail})



#SEARCH FUNCTIONS.

# Handles the search form and redirects to the page with search results.
def gsearch(request):
    # Handles the form that has been submitted.
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # k is the keyword being searched on.
            k=post.Criteria+'/'
            return redirect(k)
    # Displays the search form.
    else:
        form = SearchForm()
    return render(request, 'profilesearch/search.html', {'form': form})

# Displays the users which match the search criteria.
def ksearch(request, **kwargs):
    # Get the keyword for the search
    pseudov=str(request.user)
    for key, value in kwargs.iteritems():
        s=value;
    # Creates an array of objects that satisfy the criteria.
    userdetail= Userdetail.objects.filter(Q(Instruments__icontains=s)|Q(Genre__icontains=s)).exclude(Nickname=pseudov).order_by('Rating')
    # Renders the list of users to be displayed
    return render(request, 'profilesearch/post_list.html', {'userdetail':userdetail})


#REQUESTS.

#Displays Requests
def Requests(request):
    # Creates an array Requests sent to the user. 
    pseudov=str(request.user)
    userdetail= Crequest.objects.filter(User1=pseudov)
    #Renders the list of pending requests.
    return render(request, 'requests/req.html', {'userdetail':userdetail})



# Displays userdetails of a user with options of accepting or rejecting the request.
def reqsearch(request, **kwargs):
     # Get username of the user.
    pseudov=str(request.user)
    for key, value in kwargs.iteritems():
        s=value;
    # Get the users profile.
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





