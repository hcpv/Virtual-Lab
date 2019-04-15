from django.http import HttpResponseRedirect
from django.shortcuts import render
import re
import control
from .forms import NameForm
import os
import pandas as pd

def objective(request):
    return render(request,'StateSpace/Objectivessp.html')
def theory(request):
    return render(request,'StateSpace/Theoryss.html')
def get_name(request):
	os.chdir(os.path.dirname(__file__))
	html1=0
	html2=0
	html3=0
	html4=0
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			abc=form.cleaned_data
			n=str(abc['Numerator_Coefficients'])
			d=str(abc['Denominator_Coefficients'])
			numlst=list(map(int,n.split()))
			denumlst=list(map(int,d.split()))
			stsp=control.tf2ss(numlst,denumlst)
			A=stsp.A
			B=stsp.B
			C=stsp.C
			D=stsp.D
			df = pd.DataFrame(A)
			html1 = df.to_html(index=False,header=False)
			df = pd.DataFrame(B)
			html2 = df.to_html(index=False,header=False)
			df = pd.DataFrame(C)
			html3 = df.to_html(index=False,header=False)
			df = pd.DataFrame(D)
			html4 = df.to_html(index=False,header=False)
	else:
		form = NameForm()
	return render(request, 'StateSpace/loginssp.html', {'form': form,'A': html1,'B':html2,'C':html3,'D':html4})
