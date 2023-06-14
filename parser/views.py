from django.shortcuts import render

from .models import Quote

import finnhub
# Create your views here.




finnhub_client = finnhub.Client(api_key="chvcn6pr01qrqeng4legchvcn6pr01qrqeng4lf0")





def home(request) :
    quotes = Quote.objects.all()
    context = {'quotes':quotes}
    return render(request, 'parser/home.html', context)


def quote(request,name) :
    quotes = Quote.objects.filter(name=name)
    context = {'quotes':quotes}
    return render(request, 'parser/quote.html', context)