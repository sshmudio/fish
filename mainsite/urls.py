from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.MainPage.as_view(), name='index'),
    path('auth/', views.AuthPage.as_view(), name='auth'),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
