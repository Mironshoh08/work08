import requests
from django.http import JsonResponse
from django.shortcuts import render


def get_exchange_rate(request):
    url = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/'
    response = requests.get(url)
    data = response.json()

    if request.method == 'POST':
        from_currency = request.POST.get('from_currency')
        to_currency = request.POST.get('to_currency')
        amount = float(request.POST.get('amount'))

        from_rate = next(item for item in data if item["Ccy"] == from_currency)["Rate"]
        to_rate = next(item for item in data if item["Ccy"] == to_currency)["Rate"]

        from_rate = float(from_rate.replace(',', ''))
        to_rate = float(to_rate.replace(',', ''))

        converted_amount = amount * (to_rate / from_rate)
        return JsonResponse({'converted_amount': converted_amount, 'to_currency': to_currency})

    return render(request, 'exchange/index.html', {'data': data})
