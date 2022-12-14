import os

import requests

url = f"https://api.apilayer.com/exchangerates_data/latest?symbols"
# url = f"https://api.apilayer.com/exchangerates_data/latest?symbols={symbols}&base={base}"

payload = {}
headers = {
    "apikey": os.getenv('APIKEY')
}

response = requests.request("GET", url, headers=headers, data=payload)

status_code = response.status_code
result = response.text
print(result)


def index(request):
    to = 'USD'
    from_currency = 'EUR'
    amount = 3500

    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_currency}&amount={amount}"

    payload = {}
    headers = {
        # "apikey": os.getenv('APIKEY')
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    status_code = response.status_code
    result_str = response.text
    result_amount = data['result']

    result_amount = 'result'
    context = {'result_amount': result_amount}
    # return render(request, 'mainapp/index.html', context)
