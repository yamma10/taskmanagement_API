
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

#pathとviewを紐付ける
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('authen/', include('djoser.urls.jwt5')),
]
