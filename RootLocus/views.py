from django.http import HttpResponseRedirect
from django.shortcuts import render
from RootLocus.locusplot import locusplot
import re
from .forms import NameForm
import os

def objective(request):
    return render(request,'RootLocus/Objective.html')
def theory(request):
    return render(request,'RootLocus/Theory.html')
def get_name(request):
	os.chdir(os.path.dirname(__file__))
	rlp=None
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			abc=form.cleaned_data
			n=str(abc['Numerator_Coefficients'])
			d=str(abc['Denominator_Coefficients'])
			numlst=list(map(int,n.split()))
			denumlst=list(map(int,d.split()))
			rlp=locusplot(numlst,denumlst)
			rlp= rlp.replace('static\\', '')
	else:
		form = NameForm()
	return render(request, 'RootLocus/login.html', {'form': form,'rlp':rlp})