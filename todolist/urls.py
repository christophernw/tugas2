from django.urls import path
from todolist.views import add_task_ajax, show_todolist_json, delete_task, todolist, register, login_user, logout_user, create_task, change_status

app_name = 'todolist'

urlpatterns = [
    path('', todolist, name='todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create_task/', create_task, name='create_task'),
    path('change_status/<int:task_id>', change_status, name='change_status'),
    path('delete_task/<int:task_id>', delete_task, name='delete_task'),
    path('json/', show_todolist_json, name='show_todolist_json'),
    path('add/', add_task_ajax, name='add_task_ajax'),
]