from django.urls import path
from . import views

app_name  = 'users'

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.RegisterUser.as_view(), name='signup'),
    path('thanks/', views.ThanksForRegister.as_view(), name='thanks'),
]