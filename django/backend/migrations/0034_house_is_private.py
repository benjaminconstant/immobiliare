# Generated by Django 3.2 on 2021-05-15 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0033_auto_20210512_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='is_private',
            field=models.BooleanField(default=False),
        ),
    ]