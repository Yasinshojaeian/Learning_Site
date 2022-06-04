from django.db import models

from Lesson.models import Lesson

# Create your models here.

class Practice(models.Model):
    file = models.FileField(upload_to='practice')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE,verbose_name='نام درس')
    class Meta:
        verbose_name ='تمرین '
        verbose_name_plural ='تمارین'
    def __str__(self):
        return self.lesson.name