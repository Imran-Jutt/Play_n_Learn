from django.forms import ModelForm, forms, TextInput
from .models import signUp
from django.utils.translation import gettext_lazy as _


class signUpForm(ModelForm):
    class Meta:
        model = signUp
        fields = ['U_Name', 'U_Email', 'U_Password']

    def __init__(self, *args, **kwargs):
        super(signUpForm, self).__init__(*args, **kwargs)
        self.fields['U_Name'].widget = TextInput(attrs={
            'id': 'uname',
            'class': '',
            'name': 'U_Name',
            'placeholder': 'Enter Your Name'})
        self.fields['U_Name'].label=''
        self.fields['U_Email'].widget = TextInput(attrs={
            'id': 'email',
            'class': '',
            'name': 'U_Email',
            'placeholder': 'Enter Your Email'})
        self.fields['U_Email'].label = ''
        self.fields['U_Password'].widget = TextInput(attrs={
            'id': 'password',
            'class': '',
            'type':'password',
            'name': 'U_Password',
            'placeholder': 'Enter Password'})
        self.fields['U_Password'].label = ''
    def clean_U_Name(self):
        name=self.cleaned_data['U_Name']
        return name.replace('','')