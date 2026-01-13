from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_user, name="login"),
    path('report/', views.report_issue, name="report_issue"),
    path('issues/', views.issue_list, name="issue_list"),
    path('issues/<int:pk>/', views.issue_detail, name="issue_detail"),
    path('logout/', views.logout_user, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('profile/upload-photo/', views.upload_photo, name="upload_photo"),
    path('profile/edit/', views.edit_profile, name="edit_profile"),
    path('change-password/', auth_views.PasswordChangeView.as_view(
        template_name='change_password.html',
        success_url='/profile/'
    ), name='change_password'),
    path('admin-dashboard/', views.admin_dashboard, name="admin_dashboard"),
    path('admin-dashboard/update/<int:pk>/', views.update_issue, name="update_issue"),



]
