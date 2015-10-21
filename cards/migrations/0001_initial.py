# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to=b'')),
                ('sound', models.FileField(null=True, upload_to=b'', blank=True)),
                ('description', models.TextField()),
                ('actions', jsonfield.fields.JSONField()),
                ('is_open', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Cutscene',
            fields=[
                ('card_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cards.Card')),
                ('content', models.TextField()),
            ],
            bases=('cards.card',),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('card_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cards.Card')),
                ('function', models.TextField()),
                ('impact', models.DecimalField(max_digits=9, decimal_places=1)),
            ],
            bases=('cards.card',),
        ),
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('card_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cards.Card')),
                ('HP', models.IntegerField(default=1)),
                ('monster_attack', models.IntegerField(default=1)),
            ],
            bases=('cards.card',),
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('card_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cards.Card')),
                ('weapon_attacK', models.IntegerField()),
                ('duration', models.IntegerField(default=1)),
            ],
            bases=('cards.card',),
        ),
        migrations.AddField(
            model_name='monster',
            name='weapon',
            field=models.ForeignKey(to='cards.Weapon', blank=True),
        ),
        migrations.AddField(
            model_name='card',
            name='cutscene_after',
            field=models.ForeignKey(related_name='+', blank=True, to='cards.Cutscene', null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='cutscene_before',
            field=models.ForeignKey(related_name='+', blank=True, to='cards.Cutscene', null=True),
        ),
    ]
