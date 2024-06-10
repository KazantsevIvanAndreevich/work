from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
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

status_choices = [
    ('draft', 'Черновик'),
    ('completed', 'Завершен'),
    ('in_progress', 'Реализация')
]

class Project(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование ПСР-проекта")
    reg_number = models.CharField(max_length=50, unique=True, verbose_name="Регистрационный номер")
    start_date = models.DateField(auto_now_add=True, null=True, verbose_name="Дата начала проекта")
    status = models.CharField(max_length=20, choices=status_choices, default='draft', verbose_name="Статус проекта")
    optimized_process = models.CharField(max_length=255, choices=[('MTO', 'МТО'), ('ETP', 'ЭТП'), ('SP', 'СП'),
                                                                  ('Safety', 'Безопасность'), ('Quality', 'Качество'),
                                                                  ('FEB', 'ФЭБ'),
                                                                  ('Repair', 'Ремонт/Кап. Строительство'),
                                                                  ('Office', 'Офисный')],
                                         verbose_name="Оптимизируемый процесс")
    customer = models.CharField(max_length=255, verbose_name="Заказчик проекта")
    customer_position = models.CharField(max_length=255, verbose_name="Должность заказчика")
    project_scope = models.TextField(null=True, verbose_name="Периметр проекта")
    process_boundaries = models.TextField(null=True, verbose_name="Границы процесса")
    process_owner = models.CharField(max_length=255, verbose_name="Владелец процесса")
    project_admin = models.ForeignKey(User, related_name='admin_projects', on_delete=models.SET_NULL, null=True, verbose_name="Администратор проекта")
    project_manager = models.CharField(max_length=255, verbose_name="Руководитель проекта")
    team_members = models.ManyToManyField(User, related_name='team_projects', verbose_name="Команда проекта")
    process_customers = models.CharField(max_length=255, verbose_name="Заказчики процесса")
    psr_expert = models.CharField(max_length=255, verbose_name="Эксперт от ПСР")

    key_risk = models.TextField(null=True,verbose_name="Ключевой риск")
    additional_risks = models.TextField(null=True, verbose_name="Дополнительные риски")
    completion_percentage = models.IntegerField(default=0, verbose_name="Процент завершения")
    overall_status_comment = models.TextField(null=True, verbose_name="Общий статус проекта")

    economic_effect_available = models.BooleanField(default=False, verbose_name="Наличие экономического эффекта")
    planned_economic_effect = models.DecimalField(max_digits=10, decimal_places=2,null=True, verbose_name="Плановая величина экономического эффекта, руб.")
    actual_economic_effect = models.DecimalField(max_digits=10, decimal_places=2,null=True, verbose_name="Фактическая величина экономического эффекта, руб.")
    goal_name = models.CharField(max_length=255, verbose_name="Наименование цели")
    measurement_unit = models.CharField(max_length=50, verbose_name="Единица измерения",null=True)
    current_value = models.DecimalField(max_digits=10, decimal_places=2,null=True, verbose_name="Текущий показатель")
    target_value = models.DecimalField(max_digits=10, decimal_places=2,null=True, verbose_name="Целевой показатель")

    class Meta:
        verbose_name = "ПСР-проект"
        verbose_name_plural = "ПСР-проекты"


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