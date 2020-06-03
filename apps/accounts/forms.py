from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.utils.html import format_html, format_html_join
from django.forms.utils import ErrorList

#TODO: for custom form errors display
class DivErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()
    def as_divs(self):
        if not self: return ''
        return '<div class="field-errorlist">{}</div>'.format(''.join(['<div class="error">%s</div>' %e for e in self]))


class SignupForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {
            'username': 
                """
                <span>150 characters or fewer.</span> 
                <span>Only letters, digits and @/./+/-/_ are allowed</span>
                """,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'username'
        self.fields['email'].widget.attrs['placeholder'] = 'email'
        self.fields['password1'].widget.attrs['placeholder'] = 'password'
        self.fields['password2'].widget.attrs['placeholder'] = 'confirm password'
        
        self.fields['password1'].help_text = (
                    """
                        <span>Your password can't be too similar to your other personal information.</span>
                        <span>Your password must contain at least 8 characters.</span>
                        <span>Your password can't be a commonly used password.</span>
                        <span>Your password can't be entirely numeric.</span>
                    """
                    )    

        self.error_class = DivErrorList   #? implement custom form errors display

class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'username'
        self.fields['password'].widget.attrs['placeholder'] = 'password'
