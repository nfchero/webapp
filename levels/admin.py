from django.contrib import admin
from levels.models import Level


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('card_bg',
                    'music',
                    'name',
                    'author',
                    'turns',
                    'card_back',
                    'rating',
                    'max_bounty',)
