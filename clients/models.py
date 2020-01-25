from django.db import models

# Create your models here.


class Client(models.Model):

    first = models.CharField(max_length=250)
    last = models.CharField(max_length=250)
    age = models.IntegerField()
    #image = models.ImageField(blank=True, upload_to='/images')

    def __str__(self):
        return '{0} {1}'.format(self.first, self.last)
