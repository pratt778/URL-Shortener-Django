from django.db import models

# Create your models here.
class Url(models.Model):
    my_Url = models.CharField(max_length=300)
    uid = models.CharField(max_length=10,default=None)
    def __str__(self):

        return "url no: "+self.uid