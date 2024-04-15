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
    
class Users(models.Model):
    username = models.CharField(verbose_name="Логин", max_length=30)
    password = models.CharField(verbose_name="Пароль", max_length=30)
    email = models.EmailField(verbose_name="E-mail", max_length=200, unique=True, null=True, blank=True)
    first_name = models.CharField(verbose_name="Имя", max_length=30, null=True, blank=True)
    last_name = models.CharField(verbose_name="Фамилия", max_length=30, null=True, blank=True)
    phone = models.CharField(verbose_name="Телефон", max_length=20, null=True, blank=True)
    image = models.ImageField(verbose_name="Изображение", upload_to="imageUsers/", null=True, blank=True)
    date = models.DateTimeField(verbose_name="Дата регистрации", auto_now_add=True, db_column='date')

    class Meta:
        verbose_name="Пользователь"
        verbose_name_plural="Пользователи"
    
    def __str__(self):
        return self.username