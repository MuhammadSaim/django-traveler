from django import forms
from django.core.files.images import get_image_dimensions
from hotel.models import Hotel


class CreateHotelForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "name",
                "placeholder": "Hotel's name"
            }
        ),
        required=True
    )

    feature_image = forms.ImageField(required=True)

    latitude = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "latitude",
                "placeholder": "Latitude"
            }
        ),
        required=True
    )

    longitude = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "longitude",
                "placeholder": "Longitude"
            }
        ),
        required=True
    )

    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "address",
                "placeholder": "Address"
            }
        ),
        required=True
    )

    description = forms.Textarea(
        attrs={
            "class": "form-control",
            "id": "description",
            "required": "true"
        }
    )

    is_active = forms.BooleanField(initial=True)

    class Meta:
        model = Hotel
        fields = (
            'name',
            'feature_image',
            'latitude',
            'longitude',
            'address',
            'description',
            'is_active'
        )
        widgets = {
            'description': forms.Textarea(attrs={
                "class": "form-control",
                "id": "description",
                "required": "true"
            })
        }

    def clean(self, *args, **kwargs):
        name = self.cleaned_data.get('name')
        feature_image = self.cleaned_data.get('feature_image')
        latitude = self.cleaned_data.get('latitude')
        longitude = self.cleaned_data.get('longitude')
        address = self.cleaned_data.get('address')
        description = self.cleaned_data.get('description')
        is_active = self.cleaned_data.get('is_active')

        if not feature_image:
            self.add_error('feature_image', "Please provide a feature image.")
            raise forms.ValidationError("Please provide a feature image.")
        else:
            w, h = get_image_dimensions(feature_image)
            print([w, h])
            if w < 500:
                self.add_error('feature_image', "Width or height of the image should be greater then 500px.")
                raise forms.ValidationError("Width or height of the image should be greater then 500px.")
            if h < 500:
                self.add_error('feature_image', "Width or height of the image should be greater then 500px.")
                raise forms.ValidationError("Width or height of the image should be greater then 500px.")

        return super(CreateHotelForm, self).clean(*args, **kwargs)
