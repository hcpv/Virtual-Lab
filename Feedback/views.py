from django.http import HttpResponseRedirect
from django.shortcuts import render
from Feedback.pidplot import pidplot
from Feedback.pidplot1 import pidplot1
import re
from .forms import NameForm
import os

def objective(request):
    return render(request,'Feedback/Objective.html')
def theory(request):
    return render(request,'Feedback/Theory.html')
def get_name(request):
	os.chdir(os.path.dirname(__file__))
	pidc=None
	pidc1=None
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			abc=form.cleaned_data
			ng=str(abc['Numerator_G'])
			dg=str(abc['Denominator_G'])
			nh=str(abc['Numerator_H'])
			dh=str(abc['Denominator_H'])
			nlg=list(map(int,ng.split()))
			dlg=list(map(int,dg.split()))
			nlh=list(map(int,nh.split()))
			dlh=list(map(int,dh.split()))
			pidc=pidplot(nlg,dlg,nlh,dlh)
			pidc= pidc.replace('static\\', '')
			pidc1=pidplot1(nlg,dlg,nlh,dlh)
			print(pidc1)
			pidc1= pidc1.replace('static\\', '')
	else:
		form = NameForm()
	return render(request, 'Feedback/login.html', {'form': form,'pidc':pidc,'pidc1':pidc1})