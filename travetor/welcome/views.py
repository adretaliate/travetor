
from django.shortcuts import render_to_response

def home(request):
	return render_to_response('welcome1.html') 

def aboutus(request):
	return render_to_response('aboutus.html')

def contactus(request):
	return render_to_response('contactus.html')

def faq(request):
	return render_to_response('faq.html')

def specialpackages(request):
	return render_to_response('specialpackages.html')


# Create your views here.
