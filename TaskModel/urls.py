from django.urls import path

from . views import add_task, task_edit, delete_task, complete_task, profile, log_in, register, logout
urlpatterns = [
    path('', add_task, name='add_task'),
    path('edit/<int:id>/', task_edit, name='edit_task'),
    path('delete/<int:id>/', delete_task, name='delete_task'), 
    path('complete/<int:id>/', complete_task, name='complete_task'),
    path('profile/', profile, name='profile'),
    path('log_in/', log_in, name='log_in'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
]