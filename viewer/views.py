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
#     for muj_token in moje_tokeny:
#         labels.append(muj_token.nazev_tokenu)
#
#         count += 1
#         muj_token.poradi = count
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

        moje_tokeny = Portfolio.objects.all()  # Vytvori list objektu [obj1, obj2, obj3, ...]

        count = 0
        dolarova_hodnota = 0

        # Pridani poradi a vypocitani dolarove hodnoty
        for muj_token in moje_tokeny:

            count += 1
            muj_token.poradi = count

            dolarova_hodnota += muj_token.dolarova_hodnota

        # Vypocet procent
        for muj_token in moje_tokeny:
            muj_token.procenta = round(((100 * muj_token.dolarova_hodnota) / dolarova_hodnota), 1)

        years_line_chart = [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 2050]
        values_line_chart = [30, 40, 35, 50, 49, 60, 70, 91, 60]

        context = {
            'moje_tokeny': moje_tokeny,
            'years_line_chart': years_line_chart,
            'values_line_chart': values_line_chart,
            'dolarova_hodnota': dolarova_hodnota,
        }

        return render(request, 'index.html', context)


def grafy(request):
    return render(request, 'grafy.html')

# def staking(request):
#     return render(request, 'staking.html')

def staking(request):
    data = Portfolio.objects.all()
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

