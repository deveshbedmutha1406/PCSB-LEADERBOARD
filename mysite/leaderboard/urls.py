from django.urls import path

from django.urls import path
from . import views

from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('home/',views.home,name = 'home'),
    path('score/',views.score, name="score"),
]

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)