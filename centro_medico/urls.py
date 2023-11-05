from django.contrib import admin
from django.urls import path
from api_integration import views

urlpatterns = [
    path('', views.home, name=''),
    path('doctor', views.doctor),
    path('paciente', views.paciente),
    
    path('admin/', admin.site.urls),
    
    path('registro/paciente/', views.registrar_paciente, name='registrar_paciente'),
    path('login/paciente/', views.login_paciente, name='login_paciente'),
    
    path('registro/medico/', views.registrar_medico, name='registrar_medico'),
    path('login/medico/', views.login_medico, name='login_medico'),
    
    path('pagina_principal_paciente/', views.pagina_principal_paciente, name='pagina_principal_paciente'),
    path('pagina_principal_medico/', views.pagina_principal_medico, 
    name='pagina_principal_medico'),
]
