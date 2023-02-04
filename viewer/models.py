from django.db.models import *
from django.contrib.auth.models import User


# Create your models here.

class Portfolio(Model):
    poradi = 0
    nazev_tokenu = CharField(max_length=16)
    dolarova_hodnota = IntegerField(null=False)
    procenta = 0

    class Meta:
        db_table = 'moje_tokeny'
        ordering = ['-dolarova_hodnota', 'nazev_tokenu']