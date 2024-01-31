from django.shortcuts import render
from news.models import News

# Create your views here.

def newsPage(request):
    news = News.objects.all()

    context = {
        "news": news
    }

    return render(request, "news/index.html", context=context)