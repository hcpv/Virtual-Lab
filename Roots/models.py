from django.db import models
from django.forms import ModelForm
from math import pi

class Input(models.Model):
    Num = models.CharField(
        verbose_name=' Numerator Coefficients',max_length=500)
    Den = models.CharField(
        verbose_name=' Denominator Coefficients',max_length=500)

class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = "__all__"

# Create your models here.
