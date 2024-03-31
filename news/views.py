from django.shortcuts import get_object_or_404, render
from news.models import News
from django.db.models import F
# Create your views here.

def newsPage(request):
    news = News.objects.all()
    
    context = {
        "news": news
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
