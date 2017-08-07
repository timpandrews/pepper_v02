from django.db import models
from django.contrib.auth.models import User

class Following(models.Model):
    user = models.ForeignKey(User, related_name='following')
    following = models.ForeignKey(User, related_name='followed_by')

    class Meta:
        verbose_name_plural = "Following"
