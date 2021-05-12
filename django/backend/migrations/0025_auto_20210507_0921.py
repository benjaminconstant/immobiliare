# Generated by Django 3.2 on 2021-05-07 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0024_alter_image_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='searches',
        ),
        migrations.AddField(
            model_name='house',
            name='searches',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.search'),
            preserve_default=False,
        ),
    ]