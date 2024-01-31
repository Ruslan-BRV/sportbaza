from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=200)
    bodyNews = models.TextField(verbose_name="Новость")
    image = models.ImageField(verbose_name="Изображение", upload_to="imageNews/", null=True)
    like = models.IntegerField(verbose_name="лайк", default=0)
    dizlike = models.IntegerField(verbose_name="дизлайк", default=0)
    class Meta:
        verbose_name="Новость"
        verbose_name_plural="Новости"

    def __str__(self):
        return self.title