from django.shortcuts import render

# Create your views here.

def index(requests):
    context = {}
    context["site_name"] = "Password generator"
    return render(requests, 'pages/index.html', context)