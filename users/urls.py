from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name  = 'users'

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.RegisterUser.as_view(), name='signup'),
    path('thanks/', views.ThanksForRegister.as_view(), name='thanks'),
    path("profile/", views.ProfileUser.as_view(), name='profile'),
    path("password_change/", views.UserPasswordChange.as_view(), name='password_change'),
    
    path("password-reset/", auth_views.PasswordResetView.as_view(
            template_name="users/password_reset_form.html",
            email_template_name="users/password_reset_email.html",
            success_url=reverse_lazy("users:password_reset_done"),
        ), name="password_reset",
    ),
    
    # Маршрут для подтверждения сброса пароля
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(
            template_name="users/password_reset_done.html"
        ), name="password_reset_done",
    ),
    
    # Маршрут для ввода нового пароля
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html",
            success_url=reverse_lazy("users:password_reset_complete"),
        ), name="password_reset_confirm",
    ),
    
    # Маршрут для завершения сброса пароля
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html"
        ),name="password_reset_complete",
    ),
]