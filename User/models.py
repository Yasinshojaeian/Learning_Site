from django.db import models
from django.contrib.auth.models import AbstractUser
from django_jalali.db import models as jmodels

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50, blank=True , verbose_name='نام')
    password = models.CharField(max_length=50, blank=True , verbose_name='رمز عبور')
    family_name = models.CharField(max_length=100 , verbose_name='نام خانوادگی ')
    birth_date = jmodels.jDateField(verbose_name='تاریخ تولد')
    biography = models.TextField(verbose_name='معرفی خود ')
    phone_number = models.CharField(max_length=11 , verbose_name='شماره تلفن')
    image = models.ImageField(verbose_name='تصویر پروفایل')