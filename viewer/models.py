from django.db.models import *
from django.contrib.auth.models import User


# Create your models here.

class Portfolio(Model):
    poradi = 0
    name = CharField(max_length=16)
    amount = CharField(max_length=16)
    dollar_value = IntegerField(null=False)
    procenta = 0

    class Meta:
        db_table = 'moje_tokeny_2'
        ordering = ['-dollar_value', 'name']


class RozdeleniBlockchainCex(Model):
    user_id = IntegerField(null=False)
    datum_a_cas = DateTimeField()
    blockchain = FloatField()
    cex = FloatField()

    class Meta:
        db_table = 'rozdeleni_blockchain_cex'


class RozdeleniHodlStakingFarmingStable(Model):
    user_id = IntegerField(null=False)
    datum_a_cas = DateTimeField()
    hodl = FloatField()
    staking = FloatField()
    farming = FloatField()
    stable_coin = FloatField()

    class Meta:
        db_table = 'rozdeleni_hodl_staking_farming_stable'


class DolarovaHodnotaPortfolia(Model):
    user_id = IntegerField(null=False)
    datum_a_cas = DateTimeField()
    dolarova_hodnota = FloatField()

    class Meta:
        db_table = 'dolarova_hodnota_portfolia'
