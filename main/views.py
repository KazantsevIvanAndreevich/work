from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout as django_logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import *
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.messages import constants as messages_constants
from .models import *
from django.utils.datastructures import MultiValueDictKeyError
from django.db.models import Q
from docx import Document
import io
import os
from django.conf import settings


def home(request):
    return render(request, 'home.html')


def project_list(request):
    search_query = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')  # Фильтр по статусу

    # Создание Q-объектов для фильтрации
    filter_query = Q(name__icontains=search_query) | Q(reg_number__icontains=search_query)

    if status_filter:
        filter_query &= Q(status=status_filter)

    projects = Project.objects.filter(filter_query)

    return render(request, 'project_list.html', {'projects': projects, 'search': search_query})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})

def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'project_form.html', {'form': form})

def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'project_form.html', {'form': form})

def project_confirm_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'project_confirm_delete.html', {'project': project})


import os


def download_project_card(request, pk):
    project = get_object_or_404(Project, pk=pk)
    document_path = "main/documents/project_template.docx"

    # Debugging information
    print(f"BASE_DIR: {settings.BASE_DIR}")  # Output the BASE_DIR being used
    print(f"Document path: {document_path}")  # Output the path being used

    # Check if the file exists
    if not os.path.exists(document_path):
        raise FileNotFoundError(f"Template not found at {document_path}")
    else:
        print("File exists")  # Debugging line

    document = Document(document_path)

    for paragraph in document.paragraphs:
        if '{{ project.name }}' in paragraph.text:
            paragraph.text = paragraph.text.replace('{{ project.name }}', project.name)
        if '{{ project.reg_number }}' in paragraph.text:
            paragraph.text = paragraph.text.replace('{{ project.reg_number }}', project.reg_number)
        if '{{ project.start_date }}' in paragraph.text:
            paragraph.text = paragraph.text.replace('{{ project.start_date }}', str(project.start_date))
        if '{{ project.get_status_display }}' in paragraph.text:
            paragraph.text = paragraph.text.replace('{{ project.get_status_display }}', project.get_status_display())
        if '{{ project.optimized_process }}' in paragraph.text:
            paragraph.text = paragraph.text.replace('{{ project.optimized_process }}', project.optimized_process)
        # Add more replacements as needed

        # Save the document to a BytesIO object
    buffer = io.BytesIO()
    document.save(buffer)
    buffer.seek(0)

    # Serve the document as a downloadable file
    response = HttpResponse(buffer,
                            content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = f'attachment; filename=project_{project.pk}.docx'
    return response

def login_view(request):
    if request.method == 'POST':
        print("POST метод получен")
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"Username: {username}, Password: {password}")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("Аутентификация успешна")
            login(request, user)
            return redirect('home')  # Перенаправление на главную страницу после успешного входа
        else:
            print("Аутентификация не удалась")
            messages.error(request, 'Неправильное имя пользователя или пароль.')  # Ошибка аутентификации
            print("Сообщение об ошибке добавлено в контекст")
    else:
        print("GET метод получен")
    return render(request, 'login.html')

def logout_view(request):
    django_logout(request)
    return redirect('home')

@login_required
@user_passes_test(lambda u: u.is_staff)
def user_list(request):
    search_query = request.GET.get('search', '')
    show_inactive = request.GET.get('show_inactive', False) == 'true'

    if show_inactive:
        users = User.objects.filter(username__icontains=search_query)
    else:
        users = User.objects.filter(username__icontains=search_query, is_active=True)

    return render(request, 'user_list.html', {'users': users, 'search': search_query, 'show_inactive': show_inactive})


@login_required
@user_passes_test(lambda u: u.is_staff)
def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)

    # Убедитесь, что у пользователя есть профиль
    if not hasattr(user, 'userprofile'):
        UserProfile.objects.create(user=user)

    departments = Department.objects.all()
    roles = Role.objects.all()

    if request.method == 'POST':
        try:
            user.username = request.POST['username']
            user.last_name = request.POST['last_name']
            user.first_name = request.POST['first_name']
            user.email = request.POST['email']
            user.is_active = request.POST['is_active'] == 'true'

            profile = user.userprofile
            profile.middle_name = request.POST.get('middle_name', '')  # Добавляем значение по умолчанию
            profile.phone = request.POST.get('phone', '')  # Добавляем значение по умолчанию
            # Проверяем, существует ли ключ 'department' в POST-запросе
            if 'department' in request.POST:
                profile.department_id = request.POST['department']
            else:
                profile.department = None  # Устанавливаем значение None в случае отсутствия
            profile.position = request.POST.get('position', '')  # Добавляем значение по умолчанию
            profile.location = request.POST.get('location', '')  # Добавляем значение по умолчанию
            profile.roles.set(request.POST.getlist('roles'))

            user.save()
            profile.save()
            messages.success(request, 'Изменения успешно сохранены.')
            return redirect('user_list')
        except MultiValueDictKeyError as e:
            # Обработка ошибки, если ключ 'department' отсутствует в POST-запросе
            messages.error(request, f'Произошла ошибка: {e}')
            return redirect('user_list')

    user_roles_ids = user.userprofile.roles.values_list('id', flat=True)

    return render(request, 'user_detail.html', {
        'user': user,
        'departments': departments,
        'roles': roles,
        'user_roles_ids': list(user_roles_ids)
    })

@login_required
@user_passes_test(lambda u: u.is_staff)
def add_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, password=password)
            if user:
                UserProfile.objects.create(user=user)
                messages.success(request, 'Пользователь успешно добавлен.')
            else:
                messages.error(request, 'Не удалось создать пользователя.')
        else:
            messages.error(request, 'Пользователь с таким именем уже существует.')
        return redirect('add_user')
    return render(request, 'add_user.html')

@login_required
@user_passes_test(lambda u: u.is_staff)
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.username = request.POST['username']
        if 'password' in request.POST and request.POST['password']:
            user.set_password(request.POST['password'])
        user.save()
        messages.success(request, 'Пользователь успешно обновлен.')
        return redirect('user_list')
    return render(request, 'edit_user.html', {'user': user})

@login_required
@user_passes_test(lambda u: u.is_staff)
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('user_list')