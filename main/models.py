from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    position = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    roles = models.ManyToManyField(Role, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

# Модель для проектов
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=100)
    # Связь с моделью User через внешний ключ
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='owned_projects')

    def __str__(self):
        return self.name

# Модель для задач в проекте
class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    # Статус задачи может быть 'Не начата', 'В процессе', 'Завершена'
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Модель для справочников
class Reference(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    # Связь с пользователем, который изменил запись
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name