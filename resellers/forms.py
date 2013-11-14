from django import forms

from resellers.models import ResellerRequest

class ResellerRequestForm(forms.ModelForm):
    class Meta:
        model = ResellerRequest
