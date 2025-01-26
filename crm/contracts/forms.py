from django import forms

from .models import Contract


class ContractForm(forms.ModelForm):
    """Форма для заполнения контракта"""

    class Meta:
        model = Contract
        fields = "name", "product", "end_date", "cost", "file"
        widgets = {"end_date": forms.DateTimeInput(attrs={"type": "date"})}
