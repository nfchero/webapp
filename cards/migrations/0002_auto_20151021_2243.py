# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='monster',
            old_name='HP',
            new_name='monster_hp',
        ),
        migrations.AlterField(
            model_name='card',
            name='image',
            field=models.ImageField(upload_to=b'card_images'),
        ),
        migrations.AlterField(
            model_name='card',
            name='sound',
            field=models.FileField(null=True, upload_to=b'card_sounds', blank=True),
        ),
    ]
