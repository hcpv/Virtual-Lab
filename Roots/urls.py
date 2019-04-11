from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from Roots import views 

urlpatterns = [
    path('', views.objective,name='objective1'),
    path('simulation/',views.index,name='simulation1'),
    path('theory/', views.theory,name='theory1'),
]
urlpatterns+=staticfiles_urlpatterns()
