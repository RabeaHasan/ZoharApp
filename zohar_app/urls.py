from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('survey', views.servey),  
    path('show',views.show),  
    path('edit/<str:barcode>', views.edit),  
    path('/update/<str:barcode>', views.update),  
    path('delete/<str:barcode>', views.destroy),  
]