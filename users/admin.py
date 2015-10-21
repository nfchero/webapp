from django.contrib import admin
from users.models import Account, Player


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('email',
                    'coins',
                    'avatar',
                    'token',)


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('player_hp',
                    'player_attack',
                    'player_weapon',)
