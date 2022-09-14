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
    email = forms.EmailField(required=True)
    gender = forms.ChoiceField(choices=gnd,required=True)
    class Meta:
        model = User
        fields = ("username","email","Phone_no","gender","password1","password2")
    
    def save(self,commit = True):
        user = super(NewUserForm, self).save(commit = False)
        user.p_num = self.cleaned_data['Phone_no']
        user.email = self.cleaned_data['email']
        user.gender = self.cleaned_data['gender']
        if commit:
            user.save()
        return user
