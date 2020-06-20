from django import forms

from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fieldss = {'text'}
        label = {'text':''}