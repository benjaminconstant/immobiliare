# Generated by Django 3.2 on 2021-05-11 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0033_alter_search_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='platform',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
