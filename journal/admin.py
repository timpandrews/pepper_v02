from django.contrib import admin

from journal.models import Journal

class JournalAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'createTS', 'updateTS']
    list_display_links = ['id', 'title']
    class Meta:
        model = Journal


admin.site.register(Journal, JournalAdmin)
