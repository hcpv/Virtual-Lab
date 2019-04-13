from django.http import HttpResponseRedirect
from django.shortcuts import render
from pidcontrol.pidplot import pidplot
from pidcontrol.pidplot1 import pidplot1
import re
from .forms import NameForm
import os

def objective(request):
    return render(request,'pidcontrol/Objective.html')
def theory(request):
    return render(request,'pidcontrol/Theory.html')
def get_name(request):
	os.chdir(os.path.dirname(__file__))
	pidc=None
	pidc1=None
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			abc=form.cleaned_data
			n=str(abc['Numerator_Coefficients'])
			d=str(abc['Denominator_Coefficients'])
			numlst=list(map(int,n.split()))
			denumlst=list(map(int,d.split()))
			kp=int(abc['Kp'])
			ki=int(abc['Ki'])
			kd=int(abc['Kd'])
			pidc=pidplot(numlst,denumlst,kp,ki,kd)
			pidc= pidc.replace('static\\', '')
			pidc1=pidplot1(numlst,denumlst,kp,ki,kd)
			pidc1= pidc1.replace('static\\', '')
	else:
		form = NameForm()
	return render(request, 'pidcontrol/login.html', {'form': form,'pidc':pidc,'pidc1':pidc1})