from django import forms

from news.models import Comment

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
