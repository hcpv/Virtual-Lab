from django.http import HttpResponseRedirect
from django.shortcuts import render
from NyquistPlot.nqstplot import nqstplot
import re
from .forms import NameForm
import os

def objective(request):
    return render(request,'NyquistPlot/Objectivenqst.html')
def theory(request):
    return render(request,'NyquistPlot/Theorynqst.html')
def get_name(request):
	os.chdir(os.path.dirname(__file__))
	nqst=None
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			abc=form.cleaned_data
			n=str(abc['Numerator_Coefficients'])
			d=str(abc['Denominator_Coefficients'])
			numlst=list(map(int,n.split()))
			denumlst=list(map(int,d.split()))
			nqst=nqstplot(numlst,denumlst)
			nqst= nqst.replace('static\\', '')
	else:
		form = NameForm()
	return render(request, 'NyquistPlot/loginnqst.html', {'form': form,'nqst':nqst})