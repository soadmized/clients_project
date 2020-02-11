from django.db import models
from django.urls import reverse


class Client(models.Model):

    first = models.CharField(max_length=250)
    last = models.CharField(max_length=250)
    birth = models.DateField(blank=True, null=True, help_text='(YYYY-MM-DD)')
    image = models.ImageField(blank=True, upload_to='images', verbose_name='Add photo:')

    def age(self):
        import datetime
        if self.birth == None:
            return None
        else:
            return int((datetime.date.today() - self.birth).days / 365.25)

    age = property(age)

    def __str__(self):
        return '{0} {1}'.format(self.first, self.last)

    def get_absolute_url(self):
        return reverse('client_detail', args=[str(self.id)])

    class Meta:
        ordering = ['last']
