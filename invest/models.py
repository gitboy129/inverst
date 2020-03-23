from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=30)
    password=models.IntegerField()

class lof(models.Model):
    code=models.CharField(max_length=6)
    shortname=models.CharField(max_length=16)
    longname = models.CharField(max_length=80,default='缺省值')
    lx = models.CharField(max_length=10,default='缺省值')
    pyname = models.CharField(max_length=80,default='缺省值')
    class Meta:
        verbose_name='LOF基金'
        verbose_name_plural=verbose_name
        def __str__(self):
            return self.verbose_name