from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('Survey', views.survey),  
    path('show',views.show), #done
    path('Show_Statuses',views.show_statuses), #done
    path('show_manufacturers',views.show_manufacturers), #done
    path('show_mainsites',views.show_mainsites),
    path('show_mainitems',views.show_mainitems),
    path('show_items',views.show_items),
    path('show1',views.guides1),
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
    path('add', views.add),
    path('addSurveyFromCSV', views.addFromCSV),
]