# Generated by Django 3.2.3 on 2021-05-31 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0003_alter_item_encodings'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='state',
            field=models.CharField(default='lost', max_length=10),
        ),
    ]
