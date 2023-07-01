from django import forms
from django.forms import widgets


class GuestForm(forms.Form):
    author_name = forms.CharField(max_length=50, required=True, label="Имя автора записи")
    author_email = forms.EmailField(max_length=50, required=True, label="Почта автора записи")
    text = forms.CharField(max_length=2000, required=True, label="Текст",
                           widget=widgets.Textarea(
                               attrs={"cols": 30, "rows": 5, "class": "test"}))
