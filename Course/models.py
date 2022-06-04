from django.db import models
from User.models import Teacher
from comment.models import Comment
from django.contrib.contenttypes.fields import GenericRelation
# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام دوره ')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='استاد')
    programming_languege  = models.CharField(max_length=100, verbose_name='زبان برنامه نویسی')
    image = models.ImageField(max_length=100, verbose_name='تصویر دوره')
    start_date = models.DateTimeField(verbose_name='تاریخ شروع')
    end_date = models.DateTimeField(verbose_name='تاریخ پایان')
    special = models.BooleanField(verbose_name='ویژه')
    comments = GenericRelation(Comment)

    class Meta:
        verbose_name ='دوره'
        verbose_name_plural ='دوره ها'
        
    def __str__(self):
        return self.name + ' ' + self.teacher.name +' ' + self.teacher.family_name