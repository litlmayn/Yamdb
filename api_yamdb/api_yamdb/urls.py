from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('api/', include('api.urls')),
=======
    path('api/v1/', include('api.urls')),
>>>>>>> 9f7b7f321f4eca27fa036563f764533790246120
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]
