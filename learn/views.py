#encoding:utf-8

from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	return HttpResponse(u"Learn App in First Django Project")
# Create your views here. 