from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
alum =alumni.objects.all()
rec =recruiters.objects.all()
down =download.objects.all()
placed=placement.objects.all()
profile=profiles.objects.all()
gal=gallery.objects.all()
a=[]
for i in rec:
	a.append(i.name)
a=sorted(a)
tea =team.objects.all()
def index(request):
	return render(request, 'home/home.html')

def about(request):
	return render(request, 'home/about.html')

def team(request):
	return render(request, 'home/team.html',{'tea':tea})

def alumni(request):
	return render(request, 'home/alumni.html',{'alum':alum})

def download(request):
	return render(request, 'home/download.html',{'down':down})

def notice(request):
	return render(request, 'home/notice.html')	

def profiles(request):
	return render(request, 'home/profiles.html',{'profile': profile})

def recruiters(request):
	return render(request, 'home/recruiters.html',context={'rec': rec , 'a': a})

def whyus(request):
	return render(request, 'home/whyus.html',{'placed':placed})

def gallery(request):
	return render(request, 'home/gallery.html',{'gal':gal})