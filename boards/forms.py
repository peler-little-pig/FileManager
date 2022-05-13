from django import forms
from .models import Topic


class NewTopicForm(forms.Form):
    subject = forms.CharField(max_length=255)

    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'What is on your mind?'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )

    file = forms.FileField()

    class Meta:
        model = Topic
        fields = ['subject', 'message', 'file']
