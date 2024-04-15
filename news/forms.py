from django import forms

from news.models import Comment, Users

class NewsCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_news', 'author', 'novosti']
        widgets = {
            'comment_news': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите ваш комментарий', 'rows': 4, 'cols': 20}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваше имя'}),
            'novosti': forms.HiddenInput(),
        }
        labels = {
            'comment_news': 'Комментарий',
            'author': 'Автор',
        }

    def save(self, *args, **kwargs):
        instance = super().save(commit=False)
        instance.save()
        return instance
    
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'phone', 'image']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '<PASSWORD>'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваш email',}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваше имя'},),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваше фамилию'},),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваш номер'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control',}),
            }
        labels = {
            'username': 'Логин',
            'password': '<PASSWORD>',
            'email': 'Email',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'phone': 'Телефон',
            'image': 'Изображение',
            }
        def save(self, *args, **kwargs):
        # Сохранение карточки вместе с тегами
            instance = super().save(commit=False)
            instance.save()
            return instance