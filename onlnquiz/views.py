from django.shortcuts import render
from onlnquiz.models import Exam,DMS,Power


def quizonln(request):
    results = Exam.objects.all()
    return render(request, 'index.html', {'Exam': results})

def home(request):
	return render(request,'home.html')


def mechanical(request):
	return render(request,'mechanical.html')


def dms(request):
	resultsdms = DMS.objects.all()
	return render(request,'DMS.html',{'DMS': resultsdms})

def power(request):
	resultspower = Power.objects.all()
	return render(request,'power.html',{'Power': resultspower})