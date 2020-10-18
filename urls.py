
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from clinic import views
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', views.home, name='home'),
    path('patient', TemplateView.as_view(template_name = 'clinic/patient.html'), name = 'patient'),
    path('patient', views.patient, name='patient'),
    path('patient_data1', TemplateView.as_view(template_name = 'patient/patient_data1.html'), name = 'patient_data1'),
    path('patient_data1', views.patient_data1, name='patient_data1'),
    path('patient_data2', TemplateView.as_view(template_name = 'patient/patient_data2.html'), name = 'patient_data2'),
    path('patient_data2', views.patient_data2, name='patient_data2'),
    path('patient_data3', TemplateView.as_view(template_name = 'patient/patient_data3.html'), name = 'patient_data3'),
    path('patient_data3', views.patient_data3, name='patient_data3'),
    path('patient_data4', TemplateView.as_view(template_name = 'patient/patient_data4.html'), name = 'patient_data4'),
    path('patient_data4', views.patient_data4, name='patient_data4'),
    path('researcher', TemplateView.as_view(template_name = 'clinic/researcher.html'), name = 'researcher'),
    path('researcher', views.researcher, name='researcher'),
    path('physician', TemplateView.as_view(template_name = 'clinic/physician.html'), name = 'physicianr'),
    path('physician', views.physician, name='physician'),
    path('Test', views.Test, name='Test'),


] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
