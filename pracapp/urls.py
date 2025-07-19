from django.urls import path
from . import views

urlpatterns = [
  
    path('', views.home, name='home'),  
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('submit/', views.submit, name='submit'),
    path('register/', views.register, name='register'),
    path('homepage/', views.homepage, name='homepage'),
    path('projects/', views.project_manager, name='project_manager'),
    path('add_task/', views.add_task, name='add_task'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('tasks/', views.task_manager, name='task_manager'),
    path('add_project/', views.add_project, name='add_project'),
    path('edit_task/<int:id>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:id>/', views.delete_task, name='delete_task'),

]
