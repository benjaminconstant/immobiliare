# Generated by Django 3.2 on 2021-05-06 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0018_search'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]