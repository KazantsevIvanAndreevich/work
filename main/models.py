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
    # Общие сведения о проекте
    name = models.CharField(max_length=100, null=True)
    registration_number = models.CharField(max_length=50, blank=True, null=True)
    start_date = models.DateField(auto_now_add=True)
    status_choices = [
        ('draft', 'Черновик'),
        ('completed', 'Завершен'),
        ('in_progress', 'Реализация')
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='draft')
    process_choices = [
        ('MTO', 'МТО'),
        ('ETP', 'ЭТП'),
        ('SP', 'СП'),
        ('Safety', 'Безопасность'),
        ('Quality', 'Качество'),
        ('FEB', 'ФЭБ'),
        ('Repair/Capital_Construction', 'Ремонт/Кап. Строительство'),
        ('Office', 'Офисный')
    ]
    process = models.CharField(max_length=50, choices=process_choices, null=True)

    # Вовлеченные лица и рамки проекта
    customer = models.CharField(max_length=100, null=True)
    customer_position = models.ForeignKey(User, related_name='customer_position', on_delete=models.CASCADE, null=True)
    project_scope = models.TextField(null=True)
    process_boundaries = models.TextField(null=True)
    process_owner = models.CharField(max_length=100, null=True)
    project_administrator = models.ForeignKey(User, related_name='project_administrator', on_delete=models.CASCADE, null=True)
    project_manager = models.CharField(max_length=100, null=True)
    project_team = models.ManyToManyField(User, related_name='project_team')
    process_customers = models.CharField(max_length=100, null=True)
    psr_expert = models.CharField(max_length=100, null=True)

    # Обоснование выбора
    key_risk = models.TextField(null=True)
    additional_risks = models.TextField(null=True)
    completion_percentage = models.IntegerField(default=0)
    project_status_comment = models.TextField(null=True)

    # Цели и плановый эффект
    has_economic_effect = models.BooleanField(choices=[(True, 'Да'), (False, 'Нет')])
    planned_economic_effect = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    actual_economic_effect = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    goal_name = models.CharField(max_length=100, null=True)
    unit_of_measurement = models.CharField(max_length=50, null=True)
    current_indicator = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    target_indicator = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    # Ключевые события (заполняются автоматически)
    project_start = models.DateField(null=True)
    diagnosis_target_state = models.DateField(null=True)
    improvement_implementation = models.DateField(null=True)
    results_consolidation_project_closure = models.DateField(null=True)
    post_project_monitoring = models.DateField(null=True)

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