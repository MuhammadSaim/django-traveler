from django import forms
from django.contrib.auth import (
    authenticate
)


class UserLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "username",
                "placeholder": "Username"
            }
        ),
        required=True
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "password",
                "placeholder": "Password"
            }
        )
    )

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                self.add_error('username', "You haven't register yet please register first.")
                raise forms.ValidationError("You haven't register yet please register first.")
            if not user.check_password(password):
                self.add_error('password', 'Your password is incorrect.')
                raise forms.ValidationError('password', 'Your password is incorrect.')
            if not user.is_active:
                self.add_error('username', "Your account is not active please contact to admin.")
                raise forms.ValidationError("Your account is not active please contact to admin.")
        return super(UserLoginForm, self).clean(*args, **kwargs)
