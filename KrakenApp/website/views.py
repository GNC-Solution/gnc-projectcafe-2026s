from django.shortcuts import render
from website.models import ATMSymbolKraken

def home(request):
    return render(request, "home.html")

def symbol_list(request):
    rsData = ATMSymbolKraken.objects.all()

    return render(request, "symbol_list.html", {
        'rsData': rsData
    })