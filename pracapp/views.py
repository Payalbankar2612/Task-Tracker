from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Project, Task



def home(request):
    return render(request, 'home.html')


def homepage(request):
    return render(request, 'homepage.html')


def task_manager(request):
    projects = Task.objects.all()
    return render(request, 'task.html', {'users': projects})


# Project manager view (shows all projects)
def project_manager(request):
    projects = Project.objects.all()
    return render(request, 'base.html', {'users': projects})



from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

def add_project(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        due_date = request.POST.get('due_date')
        project_id = request.POST.get('project')
        assigned_to_id = request.POST.get('assigned_to')
        status = request.POST.get('status')

        if not project_id or not assigned_to_id:
            return HttpResponse("Project and Assigned User must be selected.", status=400)

        project = get_object_or_404(Project, pk=project_id)
        assigned_to = get_object_or_404(User, pk=assigned_to_id)

        Task.objects.create(
            title=title,
            description=description,
            priority=priority,
            due_date=due_date,
            project=project,
            assigned_to=assigned_to,
            status=status
        )
        return redirect('task_manager')

    return render(request, 'add_project.html', {
        'projects': Project.objects.all(),
        'users': User.objects.all()
    })


def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        owner_id = request.POST.get('owner')

        owner = get_object_or_404(User, pk=owner_id)

        Project.objects.create(
            title=title,
            description=description,
            start_date=start_date,
            end_date=end_date,
            owner=owner
        )
        return redirect('project_manager')

    return render(request, 'add_task.html', {'users': User.objects.all()})

def edit(request, id):
    project = get_object_or_404(Project, id=id)

    if request.method == "POST":
        project.title = request.POST.get('title')
        project.description = request.POST.get('description')
        project.start_date = request.POST.get('start_date')
        project.end_date = request.POST.get('end_date')
        owner_id = request.POST.get('owner')
        project.owner = get_object_or_404(User, pk=owner_id)
        project.save()
        return redirect('project_manager')

    users = User.objects.all()
    return render(request, 'edit.html', {'project': project, 'users': users})

def delete(request, id):
    if request.method == "POST":
        project = get_object_or_404(Project, pk=id)
        project.delete()
        return redirect('project_manager')

def login_view(request):
    return render(request, 'login.html')

def submit(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not email or not password:
            return HttpResponse("Email and password are required.", status=400)

        if User.objects.filter(email=email).exists():
            return redirect('homepage')

        User.objects.create(
            username=email,
            email=email,
            password=make_password(password)
        )
        return redirect('homepage')

    return redirect('login')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')  
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('home')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('home')

        User.objects.create(
            username=name,
            email=email,
            password=make_password(password)
        )
        return redirect('login')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def edit_task(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.priority = request.POST.get('priority')
        task.due_date = request.POST.get('due_date')
        task.status = request.POST.get('status')
        
        project_id = request.POST.get('project')
        assigned_to_id = request.POST.get('assigned_to')

        task.project = get_object_or_404(Project, pk=project_id)
        task.assigned_to = get_object_or_404(User, pk=assigned_to_id)

        task.save()
        return redirect('task_manager')

    return render(request, 'add_project.html', {
        'task': task,
        'projects': Project.objects.all(),
        'users': User.objects.all()
    })

def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        task.delete()
        return redirect('task_manager')

