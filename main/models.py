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

STATUS_CHOICES = [
    ('draft', 'Черновик'),
    ('in_progress', 'Реализация'),
    ('completed', 'Завершен')
]

class Project(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование ПСР-проекта")
    registration_number = models.CharField(max_length=100, blank=True, verbose_name="Регистрационный номер")
    start_date = models.DateField(verbose_name="Дата начала проекта")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft', verbose_name="Статус проекта")
    optimized_process = models.CharField(max_length=255, choices=[('MTO', 'МТО'), ('ETP', 'ЭТП'), ('SP', 'СП'), ('Safety', 'Безопасность'), ('Quality', 'Качество'), ('FEB', 'ФЭБ'), ('Repair', 'Ремонт/Кап. Строительство'), ('Office', 'Офисный')], verbose_name="Оптимизируемый процесс")

    # Additional fields for project details
    customer = models.CharField(max_length=255, verbose_name="Заказчик проекта")
    customer_position = models.CharField(max_length=255, verbose_name="Должность заказчика")
    project_scope = models.TextField(verbose_name="Периметр проекта")
    process_boundary = models.TextField(verbose_name="Границы процесса", null=True)  # Set null=True
    process_owner = models.CharField(max_length=255, verbose_name="Владелец процесса")
    project_admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='admin_projects', verbose_name="Администратор проекта")
    project_manager = models.CharField(max_length=255, verbose_name="Руководитель проекта")
    project_team = models.ManyToManyField(User, related_name='team_projects', verbose_name="Команда проекта")
    process_customers = models.CharField(max_length=255, verbose_name="Заказчики процесса")
    psr_expert = models.CharField(max_length=255, verbose_name="Эксперт от ПСР")

    key_risk = models.TextField(verbose_name="Ключевой риск")
    additional_risks = models.TextField(verbose_name="Дополнительные риски", null=True)  # Set null=True
    completion_percentage = models.FloatField(default=0, verbose_name="Процент завершения")
    overall_status = models.TextField(verbose_name="Общий статус проекта", default='')  # Provide a default value

    economic_effect = models.CharField(max_length=3, choices=[('yes', 'да'), ('no', 'нет')], default='no', verbose_name="Наличие экономического эффекта")
    planned_economic_effect = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, null=True, verbose_name="Плановая величина экономического эффекта, руб.")
    actual_economic_effect = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, null=True, verbose_name="Фактическая величина экономического эффекта, руб.")
    goal_name = models.CharField(max_length=255, verbose_name="Наименование цели")

    # Auto-filled fields based on project plan
    # Auto-filled fields based on project plan
    start_event = models.DateField(null=True, blank=True, verbose_name="Старт проекта")
    diagnostics_event = models.DateField(null=True, blank=True, verbose_name="Диагностика и Целевое состояние")
    improvements_event = models.DateField(null=True, blank=True, verbose_name="Внедрение улучшений")
    closure_event = models.DateField(null=True, blank=True, verbose_name="Закрепление результатов и закрытие проекта")
    post_monitoring_event = models.DateField(null=True, blank=True, verbose_name="Постпроектный мониторинг")

    def __str__(self):
        return self.name
    def __str__(self):
        return self.name

# Модель для задач в проекте
class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    due_date = models.DateField(null=True)
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