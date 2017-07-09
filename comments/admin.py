from django.contrib import admin

# Register your models here.
from comments.models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'createTS', 'updateTS']
    list_display_links = ['id', 'user']
    class Meta:
        model = Comment

admin.site.register(Comment, CommentAdmin)
