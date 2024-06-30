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
            'project_scope', 'process_boundary_from','process_boundary_to', 'process_owner', 'project_admin', 'project_manager',
            'team_members', 'process_customers', 'psr_expert', 'key_risk', 'additional_risks',
            'completion_percentage', 'overall_status_comment', 'economic_effect_available', 'planned_economic_effect',
            'actual_economic_effect', 'goal_name', 'measurement_unit', 'current_value', 'target_value',
            'survey_1', 'project_start', 'current_state_building', 'production_analysis_1',
            'target_state_development', 'detailed_plan_development', 'improvements_implementation',
            'production_analysis_2', 'survey_2', 'closing_meeting'
        ]
        labels = {
            'name': 'Наименование ПСР-проекта',
            'reg_number': 'Регистрационный номер',
            'status': 'Статус проекта',
            'optimized_process': 'Оптимизируемый процесс',
            'customer': 'Заказчики процесса',
            'customer_position': 'Должность заказчика',
            'project_scope': 'Периметр проекта',
            'process_boundary_from': 'Границы процесса от',
            'process_boundary_to': 'до',
            'process_owner': 'Владелец процесса',
            'project_manager': 'Руководитель проекта',
            'team_members': 'Команда проекта',
            'process_customers': 'Заказчики процесса',
            'psr_expert': 'Специалист ПСР',
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
            'target_value': 'Целевой показатель',
            'survey_1': 'Анкетирование №1',
            'project_start': 'Старт проекта',
            'current_state_building': 'Построение текущего состояния процесса',
            'production_analysis_1': 'Производственный анализ №1',
            'target_state_development': 'Разработка целевого состояния процесса',
            'detailed_plan_development': 'Разработка детального плана мероприятий',
            'improvements_implementation': 'Внедрение улучшений',
            'production_analysis_2': 'Производственный анализ №2',
            'survey_2': 'Анкетирование №2',
            'closing_meeting': 'Завершающее совещание и закрытие проекта'

        }
        widgets = {
            'team_members': forms.CheckboxSelectMultiple,
            'project_scope': forms.TextInput(attrs={'placeholder': 'Подразделения 1, 2, 3...'}),
            'additional_risks': forms.Textarea(attrs={'placeholder': '1.\n2.\n3.'}),
            'survey_1': forms.DateInput(format='%d.%m.%Y', attrs={'type': 'date'}),
            'project_start': forms.DateInput(format='%d.%m.%Y', attrs={'type': 'date'}),
            'current_state_building': forms.DateInput(format='%d.%m.%Y', attrs={'type': 'date'}),
            'production_analysis_1': forms.DateInput(format='%d.%m.%Y', attrs={'type': 'date'}),
            'target_state_development': forms.DateInput(format='%d.%m.%Y', attrs={'type': 'date'}),
            'detailed_plan_development': forms.DateInput(format='%d.%m.%Y', attrs={'type': 'date'}),
            'improvements_implementation': forms.DateInput(format='%d.%m.%Y', attrs={'type': 'date'}),
            'production_analysis_2': forms.DateInput(format='%d.%m.%Y', attrs={'type': 'date'}),
            'survey_2': forms.DateInput(format='%d.%m.%Y', attrs={'type': 'date'}),
            'closing_meeting': forms.DateInput(format='%d.%m.%Y', attrs={'type': 'date'}),
        }
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class RoleForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['roles']