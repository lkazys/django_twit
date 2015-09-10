# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('content_text', models.CharField(max_length=140)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('deleted', models.BooleanField(default=False)),
                ('u_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
