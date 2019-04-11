from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from Bode_Plot import views 

urlpatterns = [
    path('', views.objective,name='objective2'),
    path('simulation/',views.index,name='simulation2'),
    path('theory/', views.theory,name='theory2'),
]
urlpatterns+=staticfiles_urlpatterns()
