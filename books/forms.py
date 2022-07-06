
from django import forms
from django.forms import ModelForm
from .models import Borrow
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class BorrowForm(ModelForm):
    class Meta:
        model = Borrow
        fields = [#'student_name',
            'book_title',
            'borrow_date',
            'return_date',
            #'email',
            'fine',
        ]



# Sign Up Form
class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length= 15, help_text= '*')
    first_name = forms.CharField(max_length = 30, help_text= '*')
    last_name = forms.CharField(max_length = 30, required=False) #help_text= 'Optional')
    email = forms.EmailField(max_length=200) #help_text = 'Enter valid e-mail address')
    course = forms.CharField(max_length= 35, required= True , help_text='*')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'course',
            'password1',
            'password2'
        ]