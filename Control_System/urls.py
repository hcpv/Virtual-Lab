from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from Control_System import views 


urlpatterns = [
    path('', views.home,name='home'),
    path('Bode_Plot/', include('Bode_Plot.urls')),
    path('Time_Response/', include('Time_Response.urls')),
    path('Roots/', include('Roots.urls')),
]
urlpatterns+=staticfiles_urlpatterns()
