from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('api/v1/', include('api.urls')),
=======
    path('api/', include('api.urls')),
>>>>>>> d180eeb9fd00dac7596ceebb8c408b92063f21b6
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]
