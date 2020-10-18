from django.urls import path, include
from . import views
#from django.contrib import admin
#from django.contrib.auth import views as auth_views
#from accounts import views

urlpatterns = [
    #path(r'^$', core_views.home, name='home'),
    #path('login', views.login, name='login'),
    #path('logout', views.logout, name='logout'),
    #path('accounts/', include('django.contrib.auth.urls')),
    #path('admin/', admin.site.urls),
    #path('', views.home, name='home'),
    #path('clinic/', include('django.contrib.auth.urls'))
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),


]
