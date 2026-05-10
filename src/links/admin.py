from django.contrib import admin

from links.models import Link


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'short_code',
        'clicks',
        'is_active',
    )

