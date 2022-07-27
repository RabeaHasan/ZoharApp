from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('survey', views.servey),  
    path('show',views.show),
    path('statuses',views.statuses),
    path('manufacturers',views.manufacturers),
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
]