# Generated by Django 3.2 on 2021-05-12 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0032_auto_20210511_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='platform',
            field=models.IntegerField(choices=[(1, 'Immobiliare'), (2, 'Casa Da Privato')], default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='search',
            name='link',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]