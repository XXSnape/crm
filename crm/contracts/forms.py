from django import forms

from .models import Contract


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = "__all__"
        widgets = {"end_date": forms.DateTimeInput(attrs={"type": "datetime-local"})}
