from django.shortcuts import render

from django.contrib.auth.forms import *
from django.views import generic
from django.urls import reverse_lazy

STATIC_URL = 'static/'

# Create your views here.
# Prihlasovaci formular
class SignUpForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2')


class SignUpView(generic.CreateView):

    # Pripoji vytvoreny formular
    form_class = SignUpForm
    success_url = reverse_lazy('prehled.html')  # kam nas to po prihlaseni presmeruje
    template_name = 'signup.html'