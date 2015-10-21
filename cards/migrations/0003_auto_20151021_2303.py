# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_auto_20151021_2243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weapon',
            old_name='weapon_attacK',
            new_name='weapon_attack',
        ),
    ]
