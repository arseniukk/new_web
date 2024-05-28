import feedparser
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, LoginForm, NewsForm
from .models import News
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'main/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})

@login_required
def home(request):
    return render(request, 'main/home.html')

def logout_view(request):
    logout(request)
    return redirect('login')
@login_required
def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            return redirect('view_news')
    else:
        form = NewsForm()
    return render(request, 'main/create_news.html', {'form': form})

def fetch_news_from_rss():
    feed_url = 'https://www.pravda.com.ua/rss/view_mainnews/'  # URL до RSS-каналу
    feed = feedparser.parse(feed_url)
    return feed.entries

@login_required
def view_news(request):
    # Отримуємо новини з бази даних
    local_news = News.objects.all()

    # Отримуємо новини з RSS-каналу
    rss_news = fetch_news_from_rss()

    context = {
        'local_news': local_news,
        'rss_news': rss_news,
    }

    return render(request, 'main/view_news.html', context)
