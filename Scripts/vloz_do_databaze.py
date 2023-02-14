from django.db import models
from viewer.models import *

def run():

    nazev = "DENT"
    dolarova_hodnota = "100"
    procenta = "1%"

    MojeTokeny.objects.create(
        nazev=nazev,
        dolarova_hodnota=dolarova_hodnota,
        procenta=procenta,
    )
    print(f"{nazev}, {dolarova_hodnota}, {procenta}")

