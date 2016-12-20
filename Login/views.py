#Login/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from Profile.forms import PostForm
from django.core.context_processors import csrf

# MAIN VIEWS.

# LOGIN.
@login_required(login_url="login/")
def home(request):
	return render(request,"home.html")


# REGISTER.
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
    return render(request, 'home.html')