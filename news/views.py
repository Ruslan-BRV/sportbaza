from django.shortcuts import render
from news.forms import NewsCommentForm, RegistrationForm
from news.models import News, Comment

from django.shortcuts import get_object_or_404, render
from news.models import News
from django.db.models import F
# Create your views here.

def newsPage(request):
    if request.method == "POST":
        form = NewsCommentForm(request.POST)
        if form.is_valid():
            form.save()
            news = News.objects.all()
            comments = Comment.objects.all()
            form = NewsCommentForm()
    else:
        news = News.objects.all()
        comments = Comment.objects.all()
        form = NewsCommentForm()

    context = {
        "news": news,
        "comments": comments,
        "form": form,
    }
    return render(request, "news/news.html", context=context)

def addLike(request, news_id):
    
    news = get_object_or_404(News, pk=news_id)

    news.like = F('like') + 1
    news.save()
    
    news.refresh_from_db()
    news = News.objects.all()
    
    context = {
        "news": news
    }

    return render(request, "news/news.html", context)  

def addDizlike(request, news_id):
    news = get_object_or_404(News, pk=news_id)

    news.dizlike = F('dizlike') + 1
    news.save()
    
    news.refresh_from_db()
    news = News.objects.all()
    
    context = {
        "news": news
    }

    return render(request, "news/news.html", context)  

def regUser(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = RegistrationForm()
    else:
        form = RegistrationForm()
    context = {
        "form": form,
    }
    return render(request, "news/registration.html", context=context)
