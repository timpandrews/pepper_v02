from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class CommentManager(models.Manager):
    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(CommentManager, self).filter(content_type=content_type, object_id=obj_id)
        return qs


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    comment = models.TextField()
    createTS = models.DateTimeField(auto_now=False, auto_now_add=True)
    updateTS = models.DateTimeField(auto_now=True, auto_now_add=False)

    objects = CommentManager()

    def __str__(self):
        return str(self.user.username)