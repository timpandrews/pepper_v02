from django.db import models
from django.core.urlresolvers import reverse

class Journal(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    createTS = models.DateTimeField(auto_now=False, auto_now_add=True)
    updateTS = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("journal:detail", kwargs={"id": self.id})