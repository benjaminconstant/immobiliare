from django.db import models

STATE_CHOICES = (
    (1, 'Da Ristrutturare'),
    (2, 'Buono / Abitabile'),
    (3, 'Ottimo / Ristrutturato'),
    (4, 'Nuovo / In costruzione'),
    (5, 'N.D.')
)


class Search(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=1000, null=False)
    link = models.CharField(max_length=1000, null=False)

    def __str__(self):
        return self.name


class House(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    date_publish = models.DateField(null=True)
    title = models.CharField(max_length=1000, null=True)
    link = models.CharField(max_length=1000, null=True)
    state = models.IntegerField(choices=STATE_CHOICES, null=True)
    text = models.TextField(max_length=5000, null=True)
    price = models.FloatField(null=True)
    price_mq = models.FloatField(null=True)
    mq = models.FloatField(null=True)
    costs = models.IntegerField(null=True, blank=True)
    is_interesting = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=False)
    has_changed = models.BooleanField(default=False)
    note = models.TextField(max_length=5000, null=True, blank=True)

    search = models.ForeignKey(Search, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    url = models.CharField(max_length=1000, null=True)
