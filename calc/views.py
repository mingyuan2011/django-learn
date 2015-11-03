#encoding:utf-8

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# for urls like /add/?a=4&b=5
def add(request):
	a = request.GET['a']
	b = request.GET['b']
	c = int(a) + int(b)
	return HttpResponse(str(c))


# for urls like /add/4/5
def elegantAdd(request, a, b):
	c = int(a) + int(b)
	return HttpResponse(str(c))
