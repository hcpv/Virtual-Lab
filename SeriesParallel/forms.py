from django import forms
#from django.contrib.postgres.forms import SimpleArrayField

#class NumberListForm(forms.Form):
  #  numbers = SimpleArrayField(forms.IntegerField())
class NameForm(forms.Form):
    Numerator_CoefficientsG=forms.CharField(label='Numerator Coefficients G(s)')
    Denominator_CoefficientsG=forms.CharField(label='Denominator Coefficients G(s)')
    Numerator_CoefficientsH=forms.CharField(label='Numerator Coefficients H(s)')
    Denominator_CoefficientsH=forms.CharField(label='Denominator Coefficients H(s)')