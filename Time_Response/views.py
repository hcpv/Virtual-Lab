from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from Time_Response.models import InputForm
from Time_Response.compute import compute
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
def objective(request):
    print('fuck')
    return render(request,'Time_Response/Objective.html')
def theory(request):
    return render(request,'Time_Response/Theory.html')
def index(request):
    os.chdir(os.path.dirname(__file__))
    result=None
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            result = compute(form2.num, form2.den)
            
            result= result.replace('static\\', '')
            print(result)
    else:
        form = InputForm()

    return render(request,'Time_Response/Time_Response.html',{'form': form, 'result': result})