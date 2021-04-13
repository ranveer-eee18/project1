from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from app.models import TODO,userdetail
from django import forms
from django.contrib.auth.models import User 


class signupform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2','is_staff']


class TODOform(ModelForm):
    class Meta:
        model=TODO
        fields=['title','status','priority']

class userdetailform(ModelForm):
    class Meta:
        model=userdetail
        fields=['fname','lname']

class updateform(forms.Form):
        priority=forms.IntegerField(required=False)


#  email, first_name, groups, id, is_active, is_staff, is_superuser, last_login,
#   last_name, logentry, password, todo, user_permissions, username