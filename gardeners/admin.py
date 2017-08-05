from django.contrib import admin

from gardeners.models import Following

class FollowingAdmin(admin.ModelAdmin):
    list_display = ['user', 'following']
    list_display_links = ['user']
    class Meta:
        model = Following


admin.site.register(Following, FollowingAdmin)
