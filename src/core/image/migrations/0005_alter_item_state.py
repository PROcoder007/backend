# Generated by Django 3.2.3 on 2021-05-31 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0004_item_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='state',
            field=models.CharField(max_length=10),
        ),
    ]