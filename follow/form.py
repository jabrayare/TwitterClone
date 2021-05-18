from .models import Follow
from django import forms


class FollowForm(forms.ModelForm):
    class Meta:
        model = Follow
        fields = ('follow_profile', 'user_profile')
