from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    gnd = (
        (1,'Male'),
        (2,'Female'),
        (3,'Others')
    )
    Phone_no = forms.IntegerField(required=True)
    first_name = forms.CharField(label = "First name")
    last_name = forms.CharField(label = "Last name")
    email = forms.EmailField(required=True)
    gender = forms.ChoiceField(choices=gnd,required=True)
    class Meta:
        model = User
        fields = ("username","first_name","last_name","email","Phone_no","gender","password1","password2")
    
    def save(self,commit = True):
        user = super(NewUserForm, self).save(commit = False)
        user.Phone_no = self.cleaned_data['Phone_no']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.gender = self.cleaned_data['gender']
        if commit:
            user.save()
        return user
