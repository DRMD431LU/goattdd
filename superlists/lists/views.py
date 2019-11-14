from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .models import Item
# Create your views here.
#@csrf_protect
def home_page(request):
	if request.method == 'POST':
		new_item_text = request.POST['item_text']
		Item.objects.create(text=new_item_text)
		return redirect('/')
	return render(request,'home.html')
