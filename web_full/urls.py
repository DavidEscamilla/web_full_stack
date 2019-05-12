from django.urls import path
from . import views
from . import Ajax

urlpatterns = [
     path('', views.index_view, name='index_view'),
     path('test/', Ajax.test, name='test'),
     path('datos/', Ajax.Paso_de_datos, name='Paso_de_datos'),
]
