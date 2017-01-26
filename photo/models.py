from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

def upload_location(instance, filename):
    return "%s/%s" %(instance.photo_user_id, filename)

class Photography(models.Model):
    class Meta():
        db_table = "photography"
    photo = models.ImageField(upload_to=upload_location)
    photo_user = models.ForeignKey(User)