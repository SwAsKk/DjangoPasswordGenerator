from django.shortcuts import render
import random
from main.forms import *
from django.views import View
from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(requests):
    context = {}
    context["site_name"] = "Password generator"

    lower_case = "abcdefghijklmnopqrstuvwyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWYZ"
    digit = "1234567890"
    symbols = "@#$%^&/\?"
    Use_fir =lower_case+upper_case+digit+symbols

    if requests.method == "POST":
        size = int(requests.POST.get('size', 0))
        password = "".join(random.sample(Use_fir,size))
        context['password'] = password

    return render(requests, 'pages/index.html', context)


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', context={'form': form})


    def post(self, request):
        bound_form = LoginForm(request.POST)

        if bound_form.is_valid():
            login_user = bound_form.cleaned_data['login']
            password = bound_form.cleaned_data['password']

            user = authenticate(username=login_user, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/')

        return render(request, 'login.html', context={'form':bound_form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')