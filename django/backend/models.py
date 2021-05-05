from django.db import models


class House(models.Model):
    id = models.CharField(primary_key=True, max_length=100, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    date_publish = models.DateField(null=False)
    title = models.CharField(max_length=1000, null=False)
    link = models.CharField(max_length=1000, null=False)
    state = models.CharField(max_length=1000, null=False)
    text = models.TextField(max_length=5000, null=False)
    price = models.FloatField(null=False)
    price_mq = models.FloatField(null=False)
    mq = models.FloatField(null=False)
    costs = models.IntegerField(null=True, blank=True)
    is_interesting = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=False)
    has_changed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
