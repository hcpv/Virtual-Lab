from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from Time_Response import views 

urlpatterns = [
   
    path('', views.objective,name='objective'),
    path('simulation/',views.index,name='simulation'),
    path('theory/', views.theory,name='theory'),
]
urlpatterns+=staticfiles_urlpatterns()
