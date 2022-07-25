from django import forms


class CreateReviewForm(forms.Form):
    location = forms.CharField(widget=forms.HiddenInput())
    value_of_money = forms.CharField(widget=forms.HiddenInput())
    cleanliness = forms.CharField(widget=forms.HiddenInput())
    services = forms.CharField(widget=forms.HiddenInput())
    comment = forms.CharField(
        widget=forms.Textarea(
                attrs={
                    "class": "form-control",
                    "id": "comment",
                    "required": "true"
                }
            )
    )

    def clean(self, *args, **kwargs):
        location = self.cleaned_data.get('location')
        value_of_money = self.cleaned_data.get('value_of_money')
        cleanliness = self.cleaned_data.get('cleanliness')
        services = self.cleaned_data.get('services')
        comment = self.cleaned_data.get('comment')

        if not location:
            self.add_error('rating', 'Please provide the location rating.')
            raise forms.ValidationError('Please provide the location rating.')

        if not value_of_money:
            self.add_error('value_of_money', 'Please provide the value of money rating.')
            raise forms.ValidationError('Please provide the value of many rating.')

        if not cleanliness:
            self.add_error('cleanliness', 'Please provide the cleanliness rating.')
            raise forms.ValidationError('Please provide the cleanliness rating.')

        if not services:
            self.add_error('services', 'Please provide the services rating.')
            raise forms.ValidationError('Please provide the services rating.')

        if not comment:
            self.add_error('comment', 'Please provide the comment.')
            raise forms.ValidationError('Please provide the comment.')

        return super(CreateReviewForm, self).clean(*args, **kwargs)