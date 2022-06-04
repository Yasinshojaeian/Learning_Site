from django.db import models

from Course.models import Course

# Create your models here.

class Season(models.Model):
    name = models.CharField(max_length=100,verbose_name='نام سرفصل')
    course = models.ForeignKey(Course , on_delete=models.CASCADE , verbose_name='دوره ')
    class Meta:
        verbose_name ='سرفصل'
        verbose_name_plural ='سرفصل ها'
    def __str__(self):
        return self.name + ' ' + self.course.name