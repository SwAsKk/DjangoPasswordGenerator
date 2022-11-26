from django.shortcuts import render
import random
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