from django import forms
#from django.contrib.postgres.forms import SimpleArrayField

#class NumberListForm(forms.Form):
  #  numbers = SimpleArrayField(forms.IntegerField())
class NameForm(forms.Form):
    Numerator_Coefficients=forms.CharField()
    Denominator_Coefficients=forms.CharField()