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
    class Status(models.IntegerChoices):
        UNCHECKED = 0, 'Не проверено'
        CHECKED = 1, 'Проверено'
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
    is_checked = models.BooleanField(default=False, choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)), verbose_name='Проверено')

    class Meta:
        verbose_name = "программа"
        verbose_name_plural = "программы"
    
    def bodyProg(self):
        # return self.bodyProgramm[:50] + "..."
        return u"%s..." % (self.bodyProgramm[:50],)
    bodyProg.short_description = 'Программа'

    def __str__(self):
        return self.nameProgramm