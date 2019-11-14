from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

# Create your views here.
#@csrf_protect
def home_page(request):
	if request.method == 'POST':
		return render(request, 'home.html',{
			'new_item_text': request.POST.get('item_text','Buy stuff'),
			})
	#	return HttpResponse(request.POST['item_text'])
	return render(request, 'home.html')
	#return HttpResponse('<html><title>To-Do lists</title></html>')
