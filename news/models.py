from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=200)
    bodyNews = models.TextField(verbose_name="Новость")
    image = models.ImageField(verbose_name="Изображение", upload_to="imageNews/", null=True)
    like = models.IntegerField(verbose_name="лайк", default=0)
    dizlike = models.IntegerField(verbose_name="дизлайк", default=0)
    upload_date = models.DateTimeField(verbose_name="дата загрузки", auto_now_add=True, db_column='upload_date')
    
    class Meta:
        verbose_name="Новость"
        verbose_name_plural="Новости"

    def bodyNew(self):
        # return self.bodyProgramm[:50] + "..."
        return u"%s..." % (self.bodyNews[:50],)
    bodyNew.short_description = 'Новость'

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    author = models.TextField(verbose_name='автор', max_length=30)
    comment_news = models.TextField(verbose_name='Сообщение')
    date_comment = models.DateTimeField(verbose_name='Дата комментария', auto_now_add=True,)
    novosti = models.ForeignKey(News, on_delete=models.CASCADE)

    class Meta:
        verbose_name="Комментарий"
        verbose_name_plural="Комментарии"

    def __str__(self):
        return self.author