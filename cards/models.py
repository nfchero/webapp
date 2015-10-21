from django.db import models
from jsonfield import JSONField

"""JSONField is a generic textfield that neatly serializes/unserializes
    JSON objects seamlessly"""


class Card(models.Model):
    """Base card model"""
    name = models.CharField(max_length=30)
    image = models.ImageField()
    sound = models.FileField(null=True, blank=True)
    description = models.TextField()
    # interesante este punto aqui: deja que se creen interacciones con cartas:
    actions = JSONField()
    cutscene_before = models.ForeignKey('Cutscene', null=True, blank=True, related_name='+')
    cutscene_after = models.ForeignKey('Cutscene', null=True, blank=True, related_name='+')
    is_open = models.BooleanField()

    class META:
        abstract = True


class Monster(Card):
    HP = models.IntegerField(default=1)
    # duda aqui en attack: su ataque no seria igual a weapon?:
    monster_attack = models.IntegerField(default=1)
    weapon = models.ForeignKey('Weapon', blank=True)


class Weapon(Card):
    weapon_attacK = models.IntegerField()
    duration = models.IntegerField(default=1)


class Item(Card):
    function = models.TextField()
    impact = models.DecimalField(max_digits=9, decimal_places=1)


class Cutscene(Card):
    content = models.TextField()
