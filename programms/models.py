from django.db import models

# Create your models here.
class TypeProgramms (models.Model):
    typeProgramms = models.CharField(verbose_name="Тип программы", max_length=100)

    class Meta:
        verbose_name = "тип программы"
        verbose_name_plural = "типы программ"

    def __str__(self):
        return self.typeProgramms
    

class Programms (models.Model):

    nameProgramm = models.CharField(verbose_name="Название программы", max_length=50)

    bodyProgramm = models.TextField(verbose_name="Программа тренировок")

    image = models.ImageField(verbose_name="Изображение", upload_to="imageProgramms/", null=True)

    typeProgramm = models.ForeignKey(
        TypeProgramms,
        verbose_name="тип программы",
        on_delete=models.CASCADE,
        related_name="type",
        null=True
    ) 

    class Meta:
        verbose_name = "программа"
        verbose_name_plural = "программы"

    def __str__(self):
        return self.nameProgramm