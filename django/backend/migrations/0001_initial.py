# Generated by Django 3.2 on 2021-04-28 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('date_publish', models.DateField()),
                ('title', models.CharField(max_length=1000)),
                ('link', models.CharField(max_length=1000)),
                ('text', models.TextField(max_length=5000)),
                ('price', models.FloatField()),
                ('price_mq', models.FloatField()),
                ('mq', models.FloatField()),
                ('costs', models.CharField(max_length=1000)),
            ],
        ),
    ]