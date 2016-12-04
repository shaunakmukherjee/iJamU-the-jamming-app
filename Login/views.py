#Login/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Userdetail
from django.shortcuts import get_object_or_404
from .forms import SearchForm
from django.shortcuts import redirect
from django.db.models import Q
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf


# Create your views here.

@login_required(login_url="login/")
def home(request):
	#return HttpResponse("Hello")
	return render(request,"home.html")

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
    return render_to_response('registration/registration_complete.html')

# Returns user details of selected user
def post_detail(request, pk):
    # Retrieves the user whose profile is clicked on or a 404 error.
    post = get_object_or_404(Userdetail, pk=pk)
    return render(request, 'post_details.html', {'post': post})

# Returns list of all users
def usr_list(request):
    userdetail= Userdetail.objects.order_by('Rating')
    return render(request, 'post_list.html', {'userdetail':userdetail})

# Provides the input form for search
def profilesearch(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        # Checks for form validity
        if form.is_valid():
            # Does not save the search in the database
            post = form.save(commit=False)
            #post.Criteria contains the key to be searched on.
            k=post.Criteria+'/'
            # Redirects to results
            return redirect(k)
    else:
        form = SearchForm()
    return render(request, 'search.html', {'form': form})

# Returns list of all users that satisfy the search criteria
def profiles(request, **kwargs):
    # retrieving the criteria 
    for key, value in kwargs.iteritems():
        s=value;
    # Searching in genre and instrument
    userdetail= Userdetail.objects.filter(Q(Instruments__icontains=s)|Q(Genre__icontains=s)).order_by('Rating')
    # Returning the profiles that matched the search criteria
    return render(request, 'post_list.html', {'userdetail':userdetail})
