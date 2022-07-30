from django.shortcuts import render, HttpResponse
import requests
import os


def index(request):

    url = f"https://api.apilayer.com/exchangerates_data/latest?symbols"

    headers = {
        'apikey': os.getenv('APIKEY')
    }

    response = requests.request('GET', url, headers=headers)

    result_amount = 'result'
    context = {'result_amount': result_amount}
    return render(request, 'mainapp/index.html', context)
