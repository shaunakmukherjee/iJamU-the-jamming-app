#Profile/views.py

from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Userdetail
from .forms import SearchForm,PostForm
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf 
from django.http import HttpResponseRedirect
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Update user details. (I don't know why you are using nickname...)
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

# Create profile. Right now it creates an empty profile
def post_new(request):
    form = PostForm(request.POST)
    #if isInstance(request.user,AnonymousUser):
    k=Userdetail.objects.create(Username=request.user,Fname='',Lname='',
                                Nickname=str(request.user),
                                Techlevel=0,Year=0,Rating=0,Bio='',Genre='',Address='',
                                Instruments='')
    k.save()
    form = PostForm(request.POST or None,instance = k)
    if form.is_valid():
        post = form.save(commit=True)
        post.username=request.user
        # Nickname is string representation of User
        post.Nickname=str(post.Username)
        post.save()
        return redirect('post_detail', pk=post.pk)
    return render(request, 'registration/registration_complete.html', {'form': form})


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


