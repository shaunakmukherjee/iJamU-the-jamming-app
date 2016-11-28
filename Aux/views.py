from django.shortcuts import render
from .models import Userdetails,Search
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, SearchForm
from django.shortcuts import redirect

# Create your views here.

def post_detail(request, pk):
    post = get_object_or_404(Userdetails, pk=pk)
    return render(request, 'iter/post_details.html', {'post': post})

def usr_detail(request, pk):
    post = Userdetails.objects.filter(Rating__gte=5).order_by('Rating')
    return render(request, 'iter/post_details.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'iter/post_edit.html', {'form': form})


def gsearch(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            if post.Instruments=="Drums":
                return redirect('drum/')
            else :
                return redirect('post_detail', 1)
    else:
        form = SearchForm()
    return render(request, 'iter/search.html', {'form': form})



def usr_list(request):
    userdetail= Userdetails.objects.filter(Rating__gte=5).order_by('Rating')
    return render(request, 'iter/post_list.html', {'userdetail':userdetail})

def Drums_list(request):
    userdetail= Userdetails.objects.filter(Instruments__icontains="hello").order_by('Rating')
    return render(request, 'iter/post_list.html', {'userdetail':userdetail})

