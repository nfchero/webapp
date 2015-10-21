from django.db import models
from users.models import User


class Level(models.Model):
    card_bg = models.ImageField(upload_to="level_backgrounds")
    music = models.FileField(upload_to="level_music")
    name = models.CharField(max_length=30)
    author = models.ForeignKey(User)
    turns = models.IntegerField(blank=True, null=True)
    card_back = models.ImageField(upload_to="card_backs")
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    max_bounty = models.IntegerField()
