from django import forms
# from django.contrib.auth.models import User
from .models import Detail

class DetailForm(forms.ModelForm):
    class Meta :
        model = Detail
        fields = ['name', 'email', 'address']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class' : 'form-control',
            'id'    : 'name',
        })
        self.fields['email'].widget.attrs.update({
            'class' : 'form-control',
            'id'    : 'email',
        })
        self.fields['address'].widget.attrs.update({
            'class' : 'form-control',
            'id'    : 'address',
            'rows'  : '5',
        })
