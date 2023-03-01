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
        hodl_staking_farming_stable = Dollar_value.objects.filter(category='hodl_staking_farming_stable')\
            .filter(user=User.objects.get(username="demo"))
        networks = Dollar_value.objects.filter(category='network').filter(user=User.objects.get(username="demo"))

    context = {
        'blockchain_cex': blockchain_cex,
        'hodl_staking_farming_stable': hodl_staking_farming_stable,
        'networks': networks
    }

    return render(request, 'grafy_grafy.html', context)


def grafy_tabulky(request):

    category_blockchain_cex_name = []
    category_hodl_staking_farming_stable_name = []
    network_name = []
    sorted_blockchain_cex = []
    sorted_hodl_staking_farming_stable_assets = []
    sorted_networks_assets = []

    if request.user.is_authenticated:
        blockchain_cex = Blockchain_Cex_assets.objects.all().filter(user=request.user)
        hodl_staking_farming_stable = Hodl_Staking_Farming_Stable_assets.objects.all().filter(user=request.user)
        networks = Networks_assets.objects.all().filter(user=request.user)
    else:
        blockchain_cex = Blockchain_Cex_assets.objects.all()\
            .filter(user=User.objects.get(username="demo"))
        hodl_staking_farming_stable = Hodl_Staking_Farming_Stable_assets.objects.all() \
            .filter(user=User.objects.get(username="demo"))
        networks = Networks_assets.objects.all()\
            .filter(user=User.objects.get(username="demo"))

    for category in blockchain_cex:
        if category.division not in category_blockchain_cex_name:
            category_blockchain_cex_name.append(category.division)

    for i in range(len(category_blockchain_cex_name)):
        sorted_blockchain_cex.append([])

    for category in blockchain_cex:
        for i in range(len(category_blockchain_cex_name)):
            if category.division == category_blockchain_cex_name[i]:
                sorted_blockchain_cex[i].append(category)

    for category in hodl_staking_farming_stable:
        if category.division not in category_hodl_staking_farming_stable_name:
            category_hodl_staking_farming_stable_name.append(category.division)

    for i in range(len(category_hodl_staking_farming_stable_name)):
        sorted_hodl_staking_farming_stable_assets.append([])

    for category in hodl_staking_farming_stable:
        for i in range(len(category_hodl_staking_farming_stable_name)):
            if category.division == category_hodl_staking_farming_stable_name[i]:
                sorted_hodl_staking_farming_stable_assets[i].append(category)

    for network in networks:
        if network.division not in network_name:
            network_name.append(network.division)

    for i in range(len(network_name)):
        sorted_networks_assets.append([])

    for network in networks:
        for i in range(len(network_name)):
            if network.division == network_name[i]:
                sorted_networks_assets[i].append(network)

    print(sorted_networks_assets)

    context = {
        'sorted_blockchain_cex': sorted_blockchain_cex,
        'sorted_hodl_staking_farming_stable_assets': sorted_hodl_staking_farming_stable_assets,
        'sorted_networks_assets': sorted_networks_assets,
    }

    return render(request, 'grafy_tabulky.html', context)


def staking(request):
    data = Portfolio_assets.objects.all()
    context = {'data': data}
    return render(request, 'error.html', context)


def farmy(request):
    return render(request, 'error.html')


def ceny_tokenu(request):
    return render(request, 'error.html')


def fast_api(request):
    return render(request, 'error.html')


def system(request):
    return render(request, 'error.html')


def settings(request):
    return render(request, 'settings.html')

