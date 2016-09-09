from django.shortcuts import render
from main.models import *
from django.http import HttpResponse, HttpRequest
from django.template.loader import render_to_string

# Create your views here.
def home(request):
	tovars = []
	for x in range(0, 3):
		tovars.append(x)
	context= {
		'title': 'Helloworld',
		'tovars': tovars,
	}
	return HttpResponse(render_to_string('index.html', context))