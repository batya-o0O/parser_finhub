from summer.celery import app
from .models import Quote
import finnhub
import datetime

finnhub_client = finnhub.Client(api_key="chvcn6pr01qrqeng4legchvcn6pr01qrqeng4lf0")

@app.task
def task_one():
    print(" task one called and worker is running good")
    return "success"

@app.task
def parsing():
    apple = finnhub_client.quote('AAPL')
    bitcoin = finnhub_client.quote('BTC')
    microsoft = finnhub_client.quote('MSFT')
    amazon = finnhub_client.quote('AMZN')
    tesla = finnhub_client.quote('TSLA')

    if apple['d']!=None:
        apple_quote = Quote.objects.create(name="AAPL", current=apple['c'], change = apple['d'], percent_change =apple['dp'],hayday=apple['h'],lowday=apple['l'],openday=apple['o'],prevclose=apple['pc'], time =datetime.datetime.fromtimestamp(apple['t']) )
    
    if bitcoin['d']!=None:
        bitcoin_quote = Quote.objects.create(name="BTC", current=bitcoin['c'], change = bitcoin['d'], percent_change =bitcoin['dp'],hayday=bitcoin['h'],lowday=bitcoin['l'],openday=bitcoin['o'],prevclose=bitcoin['pc'], time =datetime.datetime.fromtimestamp(bitcoin['t']) )
    
    if microsoft['d']!=None:
        microsoft_quote = Quote.objects.create(name="MSFT", current=microsoft['c'], change = microsoft['d'], percent_change =microsoft['dp'],hayday=microsoft['h'],lowday=microsoft['l'],openday=microsoft['o'],prevclose=microsoft['pc'], time =datetime.datetime.fromtimestamp(microsoft['t']) )

    if amazon['d']!=None:
        amazon_quote = Quote.objects.create(name="AMZN", current=amazon['c'], change = amazon['d'], percent_change =amazon['dp'],hayday=amazon['h'],lowday=amazon['l'],openday=amazon['o'],prevclose=amazon['pc'], time =datetime.datetime.fromtimestamp(amazon['t']) )
        
    if tesla['d']!=None:
        tesla_quote = Quote.objects.create(name="TSLA", current=tesla['c'], change = tesla['d'], percent_change =tesla['dp'],hayday=tesla['h'],lowday=tesla['l'],openday=tesla['o'],prevclose=tesla['pc'], time =datetime.datetime.fromtimestamp(tesla['t']) )

    
    return "success"
