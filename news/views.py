from django.shortcuts import render
from news.forms import NewsCommentForm
from news.models import News, Comment

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
