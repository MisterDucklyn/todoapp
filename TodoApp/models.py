from django.db import models

# Create your models here.
class Todo(models.Model):
    secimler = [
        ('True','Tamamlandi'),
        ('False','Tamamlanmadi')
    ]
    description = models.CharField(max_length=100,verbose_name='Aciglama')
    status= models.CharField(verbose_name='Status',max_length=20,choices=secimler,default=secimler[1][0])
    created_at = models.DateTimeField(verbose_name='Tarix',auto_now_add=True)