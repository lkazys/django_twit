# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twit', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='content_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='tweet',
            old_name='u_id',
            new_name='user',
        ),
    ]
