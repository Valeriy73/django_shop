from django.shortcuts import render
from main.models import *
from django.http import HttpResponse, HttpRequest
from django.template.loader import render_to_string

# Create your views here.
def home(request):
	context= {
		'title': 'Helloworld'
	}
	return HttpResponseren(render_to_string('index.html', context))