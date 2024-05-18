from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . import models
from .models import Task
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username = username):
            messages.error(request, 'Username already exists, Please choose another username')
            return redirect('signup')
        
        if User.objects.filter(email = email):
            messages.error(request, 'Account with this email already exists. Please login to your account')
            return redirect('signup')
        
        if pass1 != pass2 :
            messages.error(request, "Passwords you enter doesn't match, Try again")
            return redirect('signup')

        user = User.objects.create_user(username, email, pass1)
        user.save()
        

    return render(request, 'signup.html')


def user_login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['pass1']

        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect('todo')
            
        else:
            messages.error(request, "Incorrect login details")
    return render(request, 'login.html')

@login_required
def todolist(request):
    if request.method == 'POST':
        title = request.POST['title']
        task = models.Task(title = title, user=request.user)
        task.save()
        return redirect('todo')
    

    result = models.Task.objects.filter(user = request.user).order_by('-create')

    return render(request, 'todo.html', {'res': result}) 

@login_required
def task_delete(request, id):
    task = models.Task.objects.get(id=id, user=request.user)
    task.delete()
    return redirect('todo')


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task

@csrf_exempt
@login_required
def update_task_completion(request, task_id):
    if request.method == 'POST':
        try:
            task = Task.objects.get(id=task_id)
            complete = request.POST.get('complete') == 'true'
            task.complete = complete
            task.save()
            return JsonResponse({'success': True})
        except Task.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Task not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})


def user_logout(request):
    logout(request)
    return redirect('login')

def update_todo(request, id):
    return render(request, 'update.html')
