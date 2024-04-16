from django.urls import path,include
from . import views

urlpatterns = [

    path('addtask',views.addTask,name='addTask'),
    path('markasdone/<int:id>/', views.markAsDone,name='markAsDone'),
    path('markasundone/<int:id>/', views.markAsunDone,name='markAsunDone'),
    path('edit/<int:id>/', views.edit,name='edit'),
    path('delete/<int:id>/', views.delete,name='delete'),
    
]
