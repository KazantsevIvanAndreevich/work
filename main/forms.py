from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'name', 'registration_number', 'start_date', 'status', 'optimized_process',
            'customer', 'customer_position', 'project_scope', 'process_boundary',
            'process_owner', 'project_admin', 'project_manager', 'project_team',
            'process_customers', 'psr_expert', 'key_risk', 'additional_risks',
            'completion_percentage', 'overall_status', 'economic_effect',
            'planned_economic_effect', 'actual_economic_effect', 'goal_name'
        ]
        labels = {
            'name': 'Наименование ПСР-проекта',
            'registration_number': 'Регистрационный номер',
            'start_date': 'Дата начала проекта',
            'status': 'Статус проекта',
            'optimized_process': 'Оптимизируемый процесс',
            'customer': 'Заказчик проекта',
            'customer_position': 'Должность заказчика',
            'project_scope': 'Периметр проекта',
            'process_boundary': 'Границы процесса',
            'process_owner': 'Владелец процесса',
            'project_admin': 'Администратор проекта',
            'project_manager': 'Руководитель проекта',
            'project_team': 'Команда проекта',
            'process_customers': 'Заказчики процесса',
            'psr_expert': 'Эксперт от ПСР',
            'key_risk': 'Ключевой риск',
            'additional_risks': 'Дополнительные риски',
            'completion_percentage': 'Процент завершения',
            'overall_status': 'Общий статус проекта',
            'economic_effect': 'Наличие экономического эффекта',
            'planned_economic_effect': 'Плановая величина экономического эффекта, руб.',
            'actual_economic_effect': 'Фактическая величина экономического эффекта, руб.',
            'goal_name': 'Наименование цели'
        }

        widgets = {
            'status': forms.Select(choices=STATUS_CHOICES),
            'optimized_process': forms.Select(choices=[('MTO', 'МТО'), ('ETP', 'ЭТП'), ('SP', 'СП'), ('Safety', 'Безопасность'), ('Quality', 'Качество'), ('FEB', 'ФЭБ'), ('Repair', 'Ремонт/Кап. Строительство'), ('Office', 'Офисный')])
        }
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class RoleForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['roles']