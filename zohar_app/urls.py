from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Survey', views.survey),  
    path('show',views.show), #done
    path('Show_Statuses',views.show_statuses), #done
    path('show_manufacturers',views.show_manufacturers), #done
    path('show_mainsites',views.show_mainsites),
    path('show_mainitems',views.show_mainitems),
    path('show_items',views.show_items),
    path('Edit/<int:id>', views.edit),  
    path('Update/<int:id>', views.update),  
    path('Delete/<int:id>', views.destroy),  
]