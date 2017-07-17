from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.text import slugify


class JournalManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(JournalManager, self).filter(draft=False).filter(publish__lte=timezone.now())


# TODO: Make this work
# def upload_location(instance, filename):
#     return '%s/%s' % (instance.id, filename)

class Journal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    badge = models.FileField(null=True, blank=True) #TODO ImageField, width_field, height_field
    content = models.TextField()
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    createTS = models.DateTimeField(auto_now=False, auto_now_add=True)
    updateTS = models.DateTimeField(auto_now=True, auto_now_add=False)

    objects = JournalManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("journal:detail", kwargs={"slug": self.slug})

    @property
    def get_content_type(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return content_type


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
