import requests

url = f"https://api.apilayer.com/exchangerates_data/latest?symbols"
# url = f"https://api.apilayer.com/exchangerates_data/latest?symbols={symbols}&base={base}"

payload = {}
headers = {
  "apikey": "wNKgZXAAv3DddNIVhEpu1ZV7X8xGAvwZ"
}

response = requests.request("GET", url, headers=headers, data=payload)

status_code = response.status_code
result = response.text
print(result)
