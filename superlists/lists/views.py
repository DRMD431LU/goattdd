from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .models import Item
# Create your views here.
#@csrf_protect
def home_page(request):
		return redirect('lists/the-only-list-in-the-world')		
	#return render(request,'home.html')


def view_list(request):
	items = Item.objects.all()
	return render(request, 'list.html', {'items':items})


def new_list(request):
	return redirect('/lists/the-only-list-in-the-world')
