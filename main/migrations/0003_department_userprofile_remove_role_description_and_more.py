# Generated by Django 4.2.13 on 2024-05-22 18:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_permission_alter_role_name_role_permissions'),
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
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middle_name', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('position', models.CharField(blank=True, max_length=100)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.department')),
            ],
        ),
        migrations.RemoveField(
            model_name='role',
            name='description',
        ),
        migrations.RemoveField(
            model_name='role',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='role',
            name='permissions',
        ),
        migrations.RemoveField(
            model_name='role',
            name='users',
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Permission',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='roles',
            field=models.ManyToManyField(blank=True, to='main.role'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
