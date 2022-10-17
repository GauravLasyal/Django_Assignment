from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import MovieTable

# Create your views here.


def ssearch(request):
	str=request.POST['textquery']
	str2=request.POST['sortquery']
	if str2=='rank':
		mymovies = MovieTable.objects.filter(name__contains=str).order_by('id').values()
	elif str2=='name':
		mymovies = MovieTable.objects.filter(name__contains=str).order_by('name').values()
	elif str2=='rating':
		mymovies = MovieTable.objects.filter(name__contains=str).order_by('rating').values()
	count=len(mymovies)
	
	context={
	'mymovies':mymovies,
	'count':count
	}
	
	return render(request,'all.html',context)

def home(request):
	return render(request,'HomePage.html')
