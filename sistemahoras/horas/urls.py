from django.urls import path

from . import views

app_name ="horas"

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('mi_admin/', views.go_to_admin , name='mi_admin' ),
    path('principal/', views.principal, name='principal'),
    path('altaempleado/', views.altaempleado, name='altaempleado'),
    path('buscarempleado/',views.buscarempleado,name="buscarempleado"),
    path('modificarempleado/<int:afiliado>/',views.modificarempleado, name='modificarempleado'),
    path('verdatos/',views.verdatos, name="verdatos"),
    path('descanso/', views.descaso, name="descanso"),
    path('extension/', views.extension, name="extension"),
    path('secretaria/', views.secretaria, name="secretaria"),
]