from django.http import HttpResponseRedirect
from django.shortcuts import render
from SeriesParallel.tr1 import tr1
from SeriesParallel.tr2 import tr2
import re
from .forms import NameForm
import os

def objective(request):
    return render(request,'SeriesParallel/Objective.html')
def theory(request):
    return render(request,'SeriesParallel/Theory.html')
def get_name(request):
	os.chdir(os.path.dirname(__file__))
	sp1=None
	sp2=None
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			abc=form.cleaned_data
			nG=str(abc['Numerator_CoefficientsG'])
			dG=str(abc['Denominator_CoefficientsG'])
			numlstG=list(map(int,nG.split()))
			denumlstG=list(map(int,dG.split()))
			nH=str(abc['Numerator_CoefficientsH'])
			dH=str(abc['Denominator_CoefficientsH'])
			numlstH=list(map(int,nH.split()))
			denumlstH=list(map(int,dH.split()))
			sp1=tr1(numlstG,denumlstG,numlstH,denumlstH)
			sp1= sp1.replace('static\\', '')
			sp2=tr2(numlstG,denumlstG,numlstH,denumlstH)
			sp2= sp2.replace('static\\', '')
	else:
		form = NameForm()
	return render(request, 'SeriesParallel/login.html', {'form': form,'sp1':sp1,'sp2':sp2})