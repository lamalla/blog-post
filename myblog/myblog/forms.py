from django import forms
from blog.models import *


class CommentForm(forms.ModelForm):
        post_Id = forms.IntegerField()
        class Meta:
            model = Comment
            exclude = ('date', )


        # def __init__(self, *args, **kwargs):
        #     super(CommentForm, self).__init__(*args, **kwargs)
        #     self.fields['description'].widget = TextInput(attrs={
        #         'id': 'myCustomId',
        #         'class': 'myCustomClass',
        #         'name': 'myCustomName',
        #         'placeholder': 'myCustomPlaceholder'})
