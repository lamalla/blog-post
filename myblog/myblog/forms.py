from django import forms
from blog.models import *


class CommentForm(forms.ModelForm):
        class Meta:
            model = Comment
            exclude = ('date', )
            widgets = {
            'post_Id': forms.NumberInput(attrs={
                'required': True,
                'placeholder': '0'
            }),
        }


        # def __init__(self, *args, **kwargs):
        #     super(CommentForm, self).__init__(*args, **kwargs)
        #     self.fields['description'].widget = TextInput(attrs={
        #         'id': 'myCustomId',
        #         'class': 'myCustomClass',
        #         'name': 'myCustomName',
        #         'placeholder': 'myCustomPlaceholder'})
