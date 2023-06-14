from django.shortcuts import render

from .models import Quote


# Create your views here.









def home(request) :
    quotes = Quote.objects.all()
    context = {'quotes':quotes}
    return render(request, 'parser/home.html', context)


def quote(request,name) :
    quotes = Quote.objects.filter(name=name)
    context = {'quotes':quotes}
    return render(request, 'parser/quote.html', context)
