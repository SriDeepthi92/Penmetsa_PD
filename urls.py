from django.urls import path, include
from . import views
from django.urls import include, path
from django.views.generic.base import TemplateView


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
]
