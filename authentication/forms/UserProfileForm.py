from django import forms
from django.contrib.auth import (
    get_user_model
)


User = get_user_model()


class UserProfileForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "username",
                "placeholder": "Username"
            }
        ),
        disabled=True
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "id": "email",
                "placeholder": "Email"
            }
        ),
        disabled=True
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "first_name",
                "placeholder": "First name"
            }
        ),
        required=True
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "first_name",
                "placeholder": "Last name"
            }
        ),
        required=True
    )

    avatar = forms.ImageField()

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "avatar"
        )

    def clean(self, *args, **kwargs):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        return super(UserProfileForm, self).clean(*args, **kwargs)
