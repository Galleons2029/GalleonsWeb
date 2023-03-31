from django import forms

from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        # The Meta class telling Django which model to base the form on
        # and which fields to include in the form.
        model = Topic
        fields = ['text']
        labels = {'text': ''}
        # The empty string in the labels dictionary tells Django not
        # to generate a label for the text field.


