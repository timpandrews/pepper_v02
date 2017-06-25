from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

# TODO: Make this work
# def upload_location(instance, filename):
#     return '%s/%s' % (instance.id, filename)

class Journal(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    badge = models.FileField(null=True, blank=True) #TODO ImageField, width_field, height_field
    content = models.TextField()
    createTS = models.DateTimeField(auto_now=False, auto_now_add=True)
    updateTS = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("journal:detail", kwargs={"slug": self.slug})


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Journal.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_journal_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_journal_receiver, sender=Journal)
