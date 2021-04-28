from django.db import models


class House(models.Model):
    id = models.CharField(primary_key=True, max_length=100, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    date_publish = models.DateField(null=False)
    title = models.CharField(max_length=1000, null=False)
    link = models.CharField(max_length=1000, null=False)
    text = models.TextField(max_length=5000, null=False)
    price = models.FloatField(null=False)
    price_mq = models.FloatField(null=False)
    mq = models.FloatField(null=False)
    costs = models.CharField(max_length=1000, null=False)

    def __str__(self):
        return self.title
