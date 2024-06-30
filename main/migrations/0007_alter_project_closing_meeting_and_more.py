# Generated by Django 4.2.13 on 2024-06-30 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_project_closing_meeting_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='closing_meeting',
            field=models.DateField(verbose_name='Завершающее совещание и закрытие проекта'),
        ),
        migrations.AlterField(
            model_name='project',
            name='current_state_building',
            field=models.DateField(verbose_name='Построение текущего состояния процесса'),
        ),
        migrations.AlterField(
            model_name='project',
            name='detailed_plan_development',
            field=models.DateField(verbose_name='Разработка детального плана мероприятий'),
        ),
        migrations.AlterField(
            model_name='project',
            name='improvements_implementation',
            field=models.DateField(verbose_name='Внедрение улучшений'),
        ),
        migrations.AlterField(
            model_name='project',
            name='production_analysis_1',
            field=models.DateField(verbose_name='Производственный анализ №1'),
        ),
        migrations.AlterField(
            model_name='project',
            name='production_analysis_2',
            field=models.DateField(verbose_name='Производственный анализ №2'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_start',
            field=models.DateField(verbose_name='Старт проекта'),
        ),
        migrations.AlterField(
            model_name='project',
            name='target_state_development',
            field=models.DateField(verbose_name='Разработка целевого состояния процесса'),
        ),
    ]