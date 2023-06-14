from rest_framework.decorators import api_view
from rest_framework.response import Response
from parser.models import Quote
from . serializaers import QuoteSerializaer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/:name',
    ]

    return Response(routes)

@api_view(['GET'])
def getQuotes(request):
    quotes = Quote.objects.all()
    serializaer = QuoteSerializaer(quotes, many=True)
    return Response(serializaer.data)


@api_view(['GET'])
def getQuote(request,name):
    quotes = Quote.objects.filter(name=name)
    serializaer = QuoteSerializaer(quotes, many=True)
    return Response(serializaer.data)