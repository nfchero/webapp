from django.db import models
from cards.models import Weapon


class Account(models.Model):
    email = models.CharField(max_length=40)
    coins = models.IntegerField()
    avatar = models.ImageField(upload_to="user_avatars")
    token = models.TextField()

    class META:
        abstract = True


class Player(models.Model):
    player_hp = models.IntegerField()
    player_attack = models.IntegerField()
    player_weapon = models.ForeignKey(Weapon)
