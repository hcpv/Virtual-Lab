from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from Control_System import views 


urlpatterns = [
    path('', views.home,name='home'),
    path('Bode_Plot/', include('Bode_Plot.urls')),
    path('Time_Response/', include('Time_Response.urls')),
    path('RootLocus/', include('RootLocus.urls')),
    path('Roots/', include('Roots.urls')),
    path('NyquistPlot/', include('NyquistPlot.urls')),
    path('PIDControl/', include('pidcontrol.urls')),
    path('StateSpace/', include('StateSpace.urls')),
    path('Feedback/', include('Feedback.urls')),
    path('SeriesParallel/', include('SeriesParallel.urls')),
]
urlpatterns+=staticfiles_urlpatterns()
