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
            'name', 'reg_number', 'status', 'optimized_process', 'customer', 'customer_position',
            'project_scope', 'process_boundaries', 'process_owner', 'project_admin', 'project_manager',
            'team_members', 'process_customers', 'psr_expert', 'key_risk', 'additional_risks',
            'completion_percentage', 'overall_status_comment', 'economic_effect_available', 'planned_economic_effect',
            'actual_economic_effect', 'goal_name', 'measurement_unit', 'current_value', 'target_value'
        ]
        labels = {
            'name': 'Наименование ПСР-проекта',
            'reg_number': 'Регистрационный номер',
            'status': 'Статус проекта',
            'optimized_process': 'Оптимизируемый процесс',
            'customer': 'Заказчик проекта',
            'customer_position': 'Должность заказчика',
            'project_scope': 'Периметр проекта',
            'process_boundaries': 'Границы процесса',
            'process_owner': 'Владелец процесса',
            'project_admin': 'Администратор проекта',
            'project_manager': 'Руководитель проекта',
            'team_members': 'Команда проекта',
            'process_customers': 'Заказчики процесса',
            'psr_expert': 'Эксперт от ПСР',
            'key_risk': 'Ключевой риск',
            'additional_risks': 'Дополнительные риски',
            'completion_percentage': 'Процент завершения',
            'overall_status_comment': 'Общий статус проекта',
            'economic_effect_available': 'Наличие экономического эффекта',
            'planned_economic_effect': 'Плановая величина экономического эффекта, руб.',
            'actual_economic_effect': 'Фактическая величина экономического эффекта, руб.',
            'goal_name': 'Наименование цели',
            'measurement_unit': 'Единица измерения',
            'current_value': 'Текущий показатель',
            'target_value': 'Целевой показатель'
        }
        widgets = {
            'team_members': forms.CheckboxSelectMultiple,
        }
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class RoleForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['roles']