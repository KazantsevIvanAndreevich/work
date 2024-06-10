from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import download_project_card

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/create/', views.project_create, name='project_create'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('projects/<int:pk>/update/', views.project_update, name='project_update'),
    path('projects/<int:pk>/project_confirm_delete/', views.project_confirm_delete, name='project_confirm_delete'),
    path('projects/<int:pk>/download/', download_project_card, name='project_download_card'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add_user/', views.add_user, name='add_user'),
    path('user_list/', views.user_list, name='user_list'),
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)