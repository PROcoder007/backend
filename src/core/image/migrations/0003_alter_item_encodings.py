# Generated by Django 3.2.3 on 2021-05-31 17:42

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0002_auto_20210531_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='encodings',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=20, max_digits=100), size=None), blank=True, default=list, size=None),
        ),
    ]