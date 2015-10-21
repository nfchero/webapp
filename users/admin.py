from django.contrib import admin
from cards.models import Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'image',
                    'sound',
                    'description',
                    'actions',
                    'cutscene_before',
                    'cutscene_after',
                    'is_open',)
