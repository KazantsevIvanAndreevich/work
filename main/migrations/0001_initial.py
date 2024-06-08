# Generated by Django 4.2.13 on 2024-06-08 18:36

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование ПСР-проекта')),
                ('registration_number', models.CharField(blank=True, max_length=100, verbose_name='Регистрационный номер')),
                ('start_date', models.DateField(verbose_name='Дата начала проекта')),
                ('status', models.CharField(choices=[('draft', 'Черновик'), ('in_progress', 'Реализация'), ('completed', 'Завершен')], default='draft', max_length=20, verbose_name='Статус проекта')),
                ('optimized_process', models.CharField(choices=[('MTO', 'МТО'), ('ETP', 'ЭТП'), ('SP', 'СП'), ('Safety', 'Безопасность'), ('Quality', 'Качество'), ('FEB', 'ФЭБ'), ('Repair', 'Ремонт/Кап. Строительство'), ('Office', 'Офисный')], max_length=255, verbose_name='Оптимизируемый процесс')),
                ('customer', models.CharField(max_length=255, verbose_name='Заказчик проекта')),
                ('customer_position', models.CharField(max_length=255, verbose_name='Должность заказчика')),
                ('project_scope', models.TextField(verbose_name='Периметр проекта')),
                ('process_boundary', models.TextField(null=True, verbose_name='Границы процесса')),
                ('process_owner', models.CharField(max_length=255, verbose_name='Владелец процесса')),
                ('project_manager', models.CharField(max_length=255, verbose_name='Руководитель проекта')),
                ('process_customers', models.CharField(max_length=255, verbose_name='Заказчики процесса')),
                ('psr_expert', models.CharField(max_length=255, verbose_name='Эксперт от ПСР')),
                ('key_risk', models.TextField(verbose_name='Ключевой риск')),
                ('additional_risks', models.TextField(null=True, verbose_name='Дополнительные риски')),
                ('completion_percentage', models.FloatField(default=0, verbose_name='Процент завершения')),
                ('overall_status', models.TextField(default='', verbose_name='Общий статус проекта')),
                ('economic_effect', models.CharField(choices=[('yes', 'да'), ('no', 'нет')], default='no', max_length=3, verbose_name='Наличие экономического эффекта')),
                ('planned_economic_effect', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10, null=True, verbose_name='Плановая величина экономического эффекта, руб.')),
                ('actual_economic_effect', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10, null=True, verbose_name='Фактическая величина экономического эффекта, руб.')),
                ('goal_name', models.CharField(max_length=255, verbose_name='Наименование цели')),
                ('start_event', models.DateField(blank=True, null=True, verbose_name='Старт проекта')),
                ('diagnostics_event', models.DateField(blank=True, null=True, verbose_name='Диагностика и Целевое состояние')),
                ('improvements_event', models.DateField(blank=True, null=True, verbose_name='Внедрение улучшений')),
                ('closure_event', models.DateField(blank=True, null=True, verbose_name='Закрепление результатов и закрытие проекта')),
                ('post_monitoring_event', models.DateField(blank=True, null=True, verbose_name='Постпроектный мониторинг')),
                ('project_admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='admin_projects', to=settings.AUTH_USER_MODEL, verbose_name='Администратор проекта')),
                ('project_team', models.ManyToManyField(related_name='team_projects', to=settings.AUTH_USER_MODEL, verbose_name='Команда проекта')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middle_name', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('position', models.CharField(blank=True, max_length=100)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.department')),
                ('roles', models.ManyToManyField(blank=True, to='main.role')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('due_date', models.DateField(null=True)),
                ('status', models.CharField(max_length=100)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='main.project')),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
