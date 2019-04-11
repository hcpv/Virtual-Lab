from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse

def home(request):
	return render(request,'Control_System/home.html')