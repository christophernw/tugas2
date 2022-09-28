from django.urls import path
from todolist.views import delete, todolist, register, login_user, logout_user, create_task, change_status, delete

app_name = 'todolist'

urlpatterns = [
    path('', todolist, name='todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create_task/', create_task, name='create_task'),
    path('change/<int:id>', change_status, name='change_status'),
    path('delete/<int:id>', delete, name='delete'),
]