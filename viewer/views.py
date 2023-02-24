from django.shortcuts import render
from django.http import HttpResponse
from viewer.models import *
from django.views import View
from django.views.generic import TemplateView, ListView
from django.contrib.auth.forms import *
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.
def hello(request):
    return render(request, 'hello.html')

# def prehled(request):
#     moje_tokeny = MojeTokeny.objects.all()
#
#     labels = []
#     count = 0
#     for my_token in moje_tokeny:
#         labels.append my_token.nazev_tokenu)
#
#         count += 1
#         my_token.poradi = count
#
#     # labels = ['a', 'b', 'c', 'd', 'e']
#     # values = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
#
#     years_line_chart = [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 2050]
#     values_line_chart = [30, 40, 35, 50, 49, 60, 70, 91, 60]
#
#     context = {
#         'moje_tokeny': moje_tokeny, 'labels': labels,
#         'years_line_chart': years_line_chart,
#         'values_line_chart': values_line_chart,
#     }
#
#     return render(request, 'index.html', context)


class PrehledView(View):

    def get(self, request):

        if request.user.is_authenticated:
            my_tokens = Portfolio_assets.objects.filter(user=request.user)  # Vytvori list objektu [obj1, obj2, obj3, ...]

        else:
            # Neprihlasi se, ale jen vytahne data od uzivatele demo
            my_tokens = Portfolio_assets.objects.filter(user=User.objects.get(username="demo"))

        count = 0
        dollar_value = 0

        # Pridani poradi a vypocitani dolarove hodnoty
        for my_token in my_tokens:

            count += 1
            my_token.count = count

            dollar_value += my_token.dollar_value

        # TODO Vypocet procent spocitat ve scraperu, tady jen zobrazit
        for my_token in my_tokens:
            my_token.percentages = round(((100 * my_token.dollar_value) / dollar_value), 1)

        years_line_chart = [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 2050]
        values_line_chart = [30, 40, 35, 50, 49, 60, 70, 91, 60]

        context = {
            'my_tokens': my_tokens,
            'years_line_chart': years_line_chart,
            'values_line_chart': values_line_chart,
            'dollar_value': dollar_value,
        }

        return render(request, 'index.html', context)


def grafy(request):

    if request.user.is_authenticated:
        blockchain_cex = Dollar_value.objects.filter(category='blockchain_cex').filter(user=request.user)
        hodl_staking_farming_stable = Dollar_value.objects.filter(category='hodl_staking_farming_stable')\
            .filter(user=request.user)
        networks = Dollar_value.objects.filter(category='network').filter(user=request.user)
    else:
        blockchain_cex = Dollar_value.objects.filter(category='blockchain_cex')\
            .filter(user=User.objects.get(username="demo"))
        hodl_staking_farming_stable = Dollar_value.objects.filter(category='hodl_staking_farming_stable') \
            .filter(user=User.objects.get(username="demo"))
        networks = Dollar_value.objects.filter(category='network').filter(user=User.objects.get(username="demo"))

    context = {
        'blockchain_cex': blockchain_cex,
        'hodl_staking_farming_stable': hodl_staking_farming_stable,
        'networks': networks
    }

    return render(request, 'grafy_grafy.html', context)

def grafy_tabulky(request):

    # # Rozdeleni blockchain / cex
    # rozdeleni_blockchain_cex = Blockchain_Cex_assets.objects.all()
    #
    # labels = ['Blockchain', 'Cex']
    # # values = [4000, 1000]
    # values = [rozdeleni_blockchain_cex[0].blockchain, rozdeleni_blockchain_cex[0].cex]
    #
    # # Rozdeleni hodl / staking / farming / stable
    #
    # rozdeleni_hodl = Hodl_Staking_Farming_Stable_assets.objects.all()
    #
    # labels_hodl = ['Hodl', 'Staking', 'Farming', 'Stable']
    # values_hodl = [rozdeleni_hodl[0].hodl, rozdeleni_hodl[0].staking, rozdeleni_hodl[0].farming,
    #                rozdeleni_hodl[0].stable_coin]
    #
    # context = {
    #     'labels': labels,
    #     'values': values,
    #     'labels_hodl': labels_hodl,
    #     'values_hodl': values_hodl,
    #     'rozdeleni': rozdeleni_blockchain_cex,
    # }

    return render(request, 'grafy_tabulky.html')

def staking(request):
    data = Portfolio_assets.objects.all()
    context = {'data': data}
    return render(request, 'staking.html', context)

def farmy(request):
    return render(request, 'farmy.html')

def ceny_tokenu(request):
    return render(request, 'ceny_tokenu.html')

def fast_api(request):
    return render(request, 'fast_api.html')

def system(request):
    return render(request, 'system.html')

def settings(request):
    return render(request, 'settings.html')

