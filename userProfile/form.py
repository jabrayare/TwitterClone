from .models import Profile
from django import forms


class userProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
            'birth_date',
            'state',
            'city',
            'user_image',
            'bio',
        )


class userProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
            'birth_date',
            'state',
            'city',
            'user_image',
            'bio',
        )
