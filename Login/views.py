#Login/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Userdetail,Connection
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


def Connections(request):
    s="drum"
    userdetail= Connection.objects.filter(User1="rohit")
    return render(request, 'con.html', {'userdetail':userdetail})

def post_detail(request, pk):
    post = get_object_or_404(Userdetail, pk=pk)
    return render(request, 'post_details.html', {'post': post})

def usr_list(request):
    userdetail= Userdetail.objects.order_by('Rating')
    return render(request, 'post_list.html', {'userdetail':userdetail})

def gsearch(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            k=post.Criteria+'/'
            return redirect(k)
    else:
        form = SearchForm()
    return render(request, 'search.html', {'form': form})

def ksearch(request, **kwargs):
    for key, value in kwargs.iteritems():
        s=value;
    userdetail= Userdetail.objects.filter(Q(Instruments__icontains=s)|Q(Genre__icontains=s)).order_by('Rating')
    return render(request, 'post_list.html', {'userdetail':userdetail})


def consearch(request, **kwargs):
    for key, value in kwargs.iteritems():
        s=value;
    userdetail= Userdetail.objects.filter(Q(Fname__icontains=s)).order_by('Rating')
    return render(request, 'post_list.html', {'userdetail':userdetail})