from django.shortcuts import render
from newsapi import NewsApiClient
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

# this is for home page
def index(request):
    return render(request, 'crime_report/home.html')

# this is for login 
# TODO: might have to create an Login Page
def register(request):
    form = CreateUserForm()
    context = {'form' : form}
    
    if request.method == 'POST':
        form = CreateUserForm()
        if form.is_valid():
            form.save()

    return render(request, 'register/register.html', context)

def login(request):
    return render(request, 'register/login.html')

# this is for NEWS FEED
def feed(request):
    newsapi = NewsApiClient(api_key = 'cc6efedd1a1a4f12bda95b15767966d0')
    headLines = newsapi.get_top_headlines(sources = 'bbc-news, the-verge')
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

    return render(request, 'news/news.html', context = {"myList" : myList})

# this is for Complaint Page
def comp(request):
    return render(request, 'complaint/complaint.html')

# this is for checking the complaint page 
def status(request):
    return render(request, 'status/status.html')

def location(request):
    return render(request, 'maps/maps.html')