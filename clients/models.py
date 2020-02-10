from django.db import models
from django.urls import reverse


class Client(models.Model):

    first = models.CharField(max_length=250)
    last = models.CharField(max_length=250)
    birth = models.DateField(blank=True, null=True)
    age = models.PositiveSmallIntegerField()

    image = models.ImageField(blank=True, upload_to='static/images/clients/%Y/%m/%d', help_text='150x150px', verbose_name='Ссылка картинки')

    def __str__(self):
        return '{0} {1}'.format(self.first, self.last)

    def get_absolute_url(self):
        return reverse('client_detail', args=[str(self.id)])

    class Meta:
        ordering = ['last']
