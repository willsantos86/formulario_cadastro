
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('formulario/', include('formulario.urls'), name='formulario'),
    path('admin/', admin.site.urls),
]
