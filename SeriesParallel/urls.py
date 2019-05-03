from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
path('', views.objective,name='objectivesp'),
path('simulation/',views.get_name,name='simulationsp'),
path('theory/', views.theory,name='theorysp'),
    #path('login/', LoginView.as_view(template_name='prodj/login.html'), name="login")
    ]
#urlpatterns+=staticfiles_urlpatterns()