from django.shortcuts import render, redirect
from newsapi import NewsApiClient
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required

def index(request): return render(request, 'crime_report/home.html')

def registerpage(request):
    if request.user.is_authenticated:
        return redirect('userhome')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was Created for ' + user)
                return redirect('login')
    context = {'form': form}
    return render(request, 'register/register.html', context)

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('userhome')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('userhome')
            else:
                messages.info(request, 'Username OR Password is wrong')
    context = {}
    return render(request, 'register/login.html', context)

def userhome(request):
    return render(request, 'crime_report/userhome.html')

def logoutUser(request): logout(request); return redirect('home')

# this is for NEWS FEED
def feed(request):
    newsapi = NewsApiClient(api_key='cc6efedd1a1a4f12bda95b15767966d0')
    headLines = newsapi.get_top_headlines(sources='bbc-news, the-verge')
    articles = headLines['articles']
    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
    myList = zip(news, desc, img)
    return render(request, 'news/news.html', context={"myList": myList})

# this is for checking the complaint page
@login_required(login_url='login')
def status(request): return render(request, 'status/status.html')