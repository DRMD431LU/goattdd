from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .models import Item
# Create your views here.
#@csrf_protect
def home_page(request):
	if request.method == 'POST':
		#print("hola")
		#print(request.POST['item_text'])
		Item.objects.create(text=request.POST.get('item_text', 'Buy stuff'))
		Item.objects.create(text=request.POST.get('item_text', 'Use it to fly'))
		return redirect('/')

	items = Item.objects.all()
	return render(request,'home.html', {'items': items})
