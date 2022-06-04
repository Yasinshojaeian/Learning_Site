from django.db import models
from Season.models import Season

# Create your models here.

class Lesson(models.Model):
    name = models.CharField(max_length=100)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    description = models.TextField(verbose_name='توضیحات ',null=True, blank=True)
    
    class Meta:
        verbose_name ='درس'
        verbose_name_plural ='دروس'
    def __str__(self):
        return self.name + ' ' + self.season.name