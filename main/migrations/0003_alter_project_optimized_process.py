# Generated by Django 4.2.13 on 2024-06-10 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_project_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='optimized_process',
            field=models.CharField(choices=[('MTO', 'МТО'), ('ETP', 'ЭТП'), ('SP', 'СП'), ('Safety', 'Безопасность'), ('Quality', 'Качество'), ('FEB', 'ФЭБ'), ('Repair', 'Ремонт/Кап. Строительство'), ('Office', 'Офисный')], max_length=255, verbose_name='Оптимизируемый процесс'),
        ),
    ]
