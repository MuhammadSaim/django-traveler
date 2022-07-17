from django import forms


class CreateReviewForm(forms.Form):
    rating = forms.CharField(widget=forms.HiddenInput())
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
        rating = self.cleaned_data.get('rating')
        comment = self.cleaned_data.get('comment')

        if not rating:
            self.add_error('rating', 'Please provide the rating.')
            raise forms.ValidationError('Please provide the rating.')

        if not comment:
            self.add_error('comment', 'Please provide the comment.')
            raise forms.ValidationError('Please provide the comment.')

        return super(CreateReviewForm, self).clean(*args, **kwargs)