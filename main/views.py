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


def home(request):
    return render(request, 'home.html')

def project_list(request):
    return render(request, 'project_list.html')

def project_detail(request):
    return render(request, 'project_detail.html')

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
            profile.middle_name = request.POST.get('middle_name', '')
            profile.phone = request.POST.get('phone', '')
            if 'department' in request.POST:
                profile.department_id = request.POST['department']
            else:
                profile.department = None
            profile.position = request.POST.get('position', '')
            profile.location = request.POST.get('location', '')

            selected_roles = request.POST.getlist('roles')
            profile.roles.set(selected_roles)

            user.save()
            profile.save()
            messages.success(request, 'Изменения успешно сохранены.')
            return redirect('user_list')
        except MultiValueDictKeyError as e:
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