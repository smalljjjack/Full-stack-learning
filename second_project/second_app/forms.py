from django import forms
from django.core import validators
from django.contrib.auth.models import User
from second_app.models import UserProfileInfo
'''
class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model  = User
        fileds = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
'''
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
'''
class FormName(forms.Form):
    name = forms.CharField()
    Email = forms.EmailField()
    verify_email = forms.EmailField(label="enter your Email again")
    text = forms.CharField(widget = forms.Textarea)
    botcatcher = forms.CharField(required = False,
                                widget = forms.HiddenInput,
                                validators = [validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        Email = all_clean_data['Email']
        Vmail = all_clean_data['verify_email']

        if Email != Vmail :
            raise forms.ValidationError("MAKE SURE EMAILS MATCH")

class NewUser(forms.ModelForm):
    ## validation
    class Meta():
        model = User
        fields = '__all__'
'''
