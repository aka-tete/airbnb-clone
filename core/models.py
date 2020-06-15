from django.db import models


class TimeStampedModel(models.Model):

    """ TIme Stamped Model """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
