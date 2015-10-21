# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_auto_20151021_2243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=40)),
                ('coins', models.IntegerField()),
                ('avatar', models.ImageField(upload_to=b'user_avatars')),
                ('token', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('player_hp', models.IntegerField()),
                ('player_attack', models.IntegerField()),
                ('player_weapon', models.ForeignKey(to='cards.Weapon')),
            ],
        ),
    ]
