from django.contrib import admin
from cards.models import Card, Monster, Weapon, Item, Cutscene


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


@admin.register(Monster)
class MonsterAdmin(admin.ModelAdmin):
    list_display = ('monster_hp',
                    'monster_attack',
                    'weapon',)


@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    list_display = ('weapon_attack',
                    'weapon',)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('function',
                    'impact',)


@admin.register(Cutscene)
class CutsceneAdmin(admin.ModelAdmin):
    list_display = ('content',)
