from django.shortcuts import render
from onlnquiz.models import Exam


def quizonln(request):
    results = Exam.objects.all()
    return render(request, 'index.html', {'Exam': results})
