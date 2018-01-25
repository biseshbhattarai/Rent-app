from django.db import models
from accounts.models import Profile


class Rentapp(models.Model):
    profile = models.OneToOneField(Profile, null=True)
    location = models.CharField(max_length=40)
    rooms_available = models.CharField(max_length=60)
    owner_name = models.CharField(max_length=50)
    owner_phone_no = models.IntegerField(default=0)
    image = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.owner_name



