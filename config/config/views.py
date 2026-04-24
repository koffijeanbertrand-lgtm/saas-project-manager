from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from projects.models import Project
from tasks.models import Task

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard')
        else:
            return render(request, 'login.html', {'error': 'Email ou mot de passe incorrect'})
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('/login')


@login_required(login_url='/login')
def dashboard_view(request):
    projects = Project.objects.filter(owner=request.user)
    tasks = Task.objects.filter(project__owner=request.user)
    context = {
        'projects': projects[:5],
        'projects_count': projects.count(),
        'tasks_count': tasks.count(),
        'tasks_done': tasks.filter(status='DONE').count(),
    }
    return render(request, 'dashboard.html', context)


@login_required(login_url='/login')
def projects_view(request):
    projects = Project.objects.filter(owner=request.user)
    return render(request, 'projects.html', {'projects': projects})