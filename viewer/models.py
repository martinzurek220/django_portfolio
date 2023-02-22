from django.db.models import *
from django.contrib.auth.models import User


# Create your models here.

# Poznamka: nazvy jako Portfolio_assets jsou schvalne s podtrzitkem, protoze se mi do pgadmina ulozi nazev
# viewer_portfolio_assets a ne nazev viewer_portfolioassets (slepene dohromady)


class Portfolio_assets(Model):
    poradi = 0
    user = ForeignKey(User, null=True, on_delete=SET_NULL)
    date_and_time = CharField(max_length=16, null=True)
    name = CharField(max_length=16, null=True)
    amount = CharField(max_length=16, null=True)
    dollar_value = IntegerField(null=False)
    procenta = 0

    class Meta:
        # db_table = 'moje_tokeny_3'
        ordering = ['-dollar_value', 'name']


class Blockchain_Cex_assets(Model):
    user_id = IntegerField(null=False)
    datum_a_cas = DateTimeField()
    blockchain = FloatField()
    cex = FloatField()

    # class Meta:
    #     db_table = 'rozdeleni_blockchain_cex'


class Hodl_Staking_Farming_Stable_assets(Model):
    user_id = IntegerField(null=False)
    datum_a_cas = DateTimeField()
    hodl = FloatField()
    staking = FloatField()
    farming = FloatField()
    stable_coin = FloatField()

    # class Meta:
    #     db_table = 'rozdeleni_hodl_staking_farming_stable'


class Dollar_value(Model):
    user_id = IntegerField(null=False)
    datum_a_cas = DateTimeField()
    dolarova_hodnota = FloatField()

    # class Meta:
    #     db_table = 'dolarova_hodnota_portfolia'
