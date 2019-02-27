from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name="home"),
    path('/create',views.add, name="add"),
    path('/todo/<todo_id>', views.edit, name="edit"),
    path('/todo/delete/<todo_id>', views.delete, name="delete"),
]
