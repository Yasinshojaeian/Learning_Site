from django.db import models

# Create your models here.


class Specialty(models.Model):
    CHOICES_WORKEXPERIENCE =(
        (1,'۶ ماه تا ۲ سال '),
        (2,' ۲ سال تا ۵ سال '),
        (3,'بیشتر از ۵ سال '),
    )
    name = models.CharField(max_length=60, verbose_name='نام تخصص')
    work_experience = models.IntegerField(choices = CHOICES_WORKEXPERIENCE,verbose_name='سابقه کاری')
    class Meta :
        verbose_name = 'تجربه'
        verbose_name_plural = 'تجربیات '
    def __str__(self):
         return u"%s [%s]" % (self.name, self.get_work_experience_display())