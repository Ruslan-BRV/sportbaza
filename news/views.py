from django.shortcuts import render
from news.models import News, Comment

# Create your views here.

def newsPage(request):
    news = News.objects.all()
    comments = Comment.objects.all()
    if request.method == "POST":
        author = request.POST.get('author')
        text = request.POST.get('text')
        novosti = int(request.POST.get('novosti'))
        print(author, text, novosti)
        comment = Comment.objects.create(author=author, comment_news=text, novosti_id=novosti)
        comment.save()
        
        news = News.objects.all()
        comments = Comment.objects.all()
    context = {
        "news": news,
        "comments": comments,
    }
    return render(request, "news/news.html", context=context)
