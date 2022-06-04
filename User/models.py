from django.db import models
from django_jalali.db import models as jmodels
# Import Class from App
from Specialty.models import Specialty
# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50, blank=True , verbose_name='نام')
    password = models.CharField(max_length=50, blank=True , verbose_name='رمز عبور')
    family_name = models.CharField(max_length=100 , verbose_name='نام خانوادگی ')
    birth_date = jmodels.jDateField(verbose_name='تاریخ تولد')
    biography = models.TextField(verbose_name='معرفی خود ')
    phone_number = models.CharField(max_length=11 , verbose_name='شماره تلفن')
    image = models.ImageField(verbose_name='تصویر پروفایل',upload_to='images/user')
    class Meta :
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
    def __str__(self):
        return self.name + ' ' + self.family_name
    
class Teacher(models.Model):
    name = models.CharField(max_length=100 , verbose_name='نام')
    password = models.CharField(max_length=50, blank=True , verbose_name='رمز عبور')
    family_name = models.CharField(max_length=100 , verbose_name='نام خانوادگی ')
    birth_date = jmodels.jDateField(verbose_name='تاریخ تولد')
    biography = models.TextField(verbose_name='معرفی خود ')
    phone_number = models.CharField(max_length=11 , verbose_name='شماره تلفن')
    image = models.ImageField(verbose_name='تصویر پروفایل',upload_to='images/teacher')
    specialty = models.ManyToManyField(Specialty, verbose_name='تخصص')
    social_networking = models.CharField(max_length=100 , verbose_name='آدرس شبکه اجتماعی')
    class Meta :
        verbose_name = 'استاد'
        verbose_name_plural = 'اساتید'
        
    def __str__(self):
        return self.name + ' ' + self.family_name
    