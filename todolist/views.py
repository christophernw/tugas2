from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from todolist.models import Task
from todolist.forms import TaskForm
from django.core import serializers
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import datetime

# Create your views here.
@login_required(login_url='/todolist/login/')
def todolist(request):
    list_task = Task.objects.filter(user=request.user)
    context = {
        'list_task': list_task,
        'username': request.user.username,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            Task.objects.create(title=title, description=description, date=datetime.datetime.now(), user=request.user)
            return redirect('todolist:todolist')
    else:
        form = TaskForm()

    return render(request, "add_task.html", context={"form": form})

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def show_todolist_json(request):
    data_task = Task.objects.filter(user=request.user).order_by('id')
    return HttpResponse(serializers.serialize("json", data_task), content_type="application/json")

@login_required(login_url='/todolist/login/')
def add_task_ajax(request):

    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        barang_baru = Task.objects.create(user=request.user, title=title, description=description)
        return JsonResponse({'error': False, 'msg':'Successful'})
    
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
@csrf_exempt
def delete_task(request, task_id):
    if request.method == "POST":
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        task.delete()

        return JsonResponse({'error':False})

@login_required(login_url='/todolist/login/')
@csrf_exempt
def change_status(request, task_id):
    if request.method == "POST":
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        task.is_finished = not task.is_finished
        task.save()

        return JsonResponse({'error':False})

