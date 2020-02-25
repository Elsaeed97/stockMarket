from django.shortcuts import render, redirect
from.models import Stock
# Create your views here.
#  Published Key : Add Your Publish Key
def index(request):
	import requests 
	import json 
	
	if request.method == 'POST':
		ticker = request.POST['ticker']
		api_request = requests.get("https://sandbox.iexapis.com/stable/stock/" + ticker + 
		"/batch?types=quote&token= " Your Key Goes Here" ") #'Add Your Key Here'

		try:
			api = json.loads(api_request.content)
		except Exception as e :
			api = "Error...."

		context = {
			'api' : api
		}
		return render(request, 'index.html', {'api' : api} )

	else :
		return render(request, 'index.html', {'ticker' : "Search for Stock to get Results :) "} )
	

def about(request):
	return render(request, 'about.html', {})


def add_stock(request):
	import json
	import requests

	if request.method == 'POST':
		tinker = request.POST.get("add_stock")
		stock = Stock()
		stock.tinker = tinker
		stock.save()
		return redirect('add_stock')
	else:
		tickers = Stock.objects.all()
		output = []
		for ticker_item in tickers:
			api_request = requests.get("https://sandbox.iexapis.com/stable/stock/" + str(ticker_item) + "/batch?types=quote&token=Tsk_98e7350b728d425bbc06fe0a5e74bad9")

			try:
				api = json.loads(api_request.content)
				output.append(api)
			except Exception as e :
				api = "Error...."
		context = {
			'tickers' : tickers,
			'output': output,
		}
		return render(request, 'add_stock.html',context )


def delete_stock(request):
	ticker = Stock.objects.all()
	context = {
		'ticker' : ticker
	}
	return render(request, 'delete_stock.html', context)

def delete(request, stock_id):
	item = Stock.objects.get(pk=stock_id)
	item.delete()
	return redirect('add_stock')
