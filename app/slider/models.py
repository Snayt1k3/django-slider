from django.db import models
from filer.fields.image import FilerImageField


class SliderItem(models.Model):
    image = FilerImageField(null=True, blank=True, on_delete=models.SET_NULL)
    title = models.IntegerField()

    class Meta:
        ordering = ['title']

    def __str__(self):
        return str(self.title)
