from . import views
from django.contrib import admin
from django.urls import path,re_path


urlpatterns = [
    path('', views.todoappView),
    path('addTodoItem/',views.addTodoView), 
    path('deleteTodoItem/<int:i>/', views.deleteTodoView),
]
