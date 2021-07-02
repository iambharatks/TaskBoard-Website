from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    title = forms.CharField(label='Task', widget=forms.Textarea(attrs={
        "placeholder": 'Add task',
        "class": "task",
        'rows': 1,
        'cols': 120,
    }))
    date = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'date',
        'placeholder': "YYYY-MM-DD"
    }))
    time = forms.TimeField(
        widget=forms.TimeInput(attrs={
            'placeholder': "00:00:00",
            'class': 'time',
        })
    )
    completed = forms.BooleanField(label='Completed', required=False, widget=forms.CheckboxInput(attrs={
        'class': 'completed'
    }))

    class Meta:
        model = Task
        fields = "__all__"
