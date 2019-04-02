from __future__ import unicode_literals
from django.db import models

class data(models.Model):
    username = models.CharField(max_length = 20)
    speed = models.CharField(max_length = 20)
    acceleration = models.CharField(max_length = 20)
    direction = models.CharField(max_length = 20)
    distance = models.CharField(max_length = 20)
    date = models.CharField(max_length = 20)
    timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)

    def __unicode__(self):
        return self.username
