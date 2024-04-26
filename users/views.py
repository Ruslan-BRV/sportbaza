from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from users.forms import LoginUserForm, RegisterUserForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, TemplateView
# Create your views here.

def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('news')
            else:
                form.add_error(None, 'Неверное имя пользоателя или пароль')
    else:
        form = LoginUserForm()
    return render(request, 'users/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect(reverse('users:login'))

class RegisterUser(CreateView):
    form_class = RegisterUserForm  # Указываем класс формы, который мы создали для регистрации
    template_name = 'users/register.html'  # Путь к шаблону, который будет использоваться для отображения формы
    extra_context = {'title': 'Регистрация'}  # Дополнительный контекст для передачи в шаблон
    success_url = reverse_lazy('users:thanks')

class ThanksForRegister(TemplateView):
    template_name = 'users/thanks.html'