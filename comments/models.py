from django.conf import settings
from django.db import models


# Create your models here.
from journal.models import Journal

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    journal = models.ForeignKey(Journal)
    comment = models.TextField()
    createTS = models.DateTimeField(auto_now=False, auto_now_add=True)
    updateTS = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(self.user.username)