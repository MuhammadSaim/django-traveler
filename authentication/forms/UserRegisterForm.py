from django import forms
from django.contrib.auth import (
    get_user_model
)

User = get_user_model()


class UserRegisterForm(forms.ModelForm):
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
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "id": "email",
                "placeholder": "Email"
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
    password_confirmation = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "password-confirmation",
                "placeholder": "Confirm Password"
            }
        )
    )
    terms = forms.BooleanField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password_confirmation',
            'terms'
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        email_qs = User.objects.filter(email=email)
        username_qs = User.objects.filter(username=username)
        if password != password_confirmation:
            self.add_error('password', "Both password fields should matched.")
            raise forms.ValidationError("Both password fields should matched.")
        if email_qs.exists():
            self.add_error('email', "Email is already exists try another one.")
            raise forms.ValidationError("Email is already exists try another one.")
        if username_qs.exists():
            self.add_error('username', "Username is already taken try different one.")
            raise forms.ValidationError("Username is already taken try different one.")

        return super(UserRegisterForm, self).clean(*args, **kwargs)