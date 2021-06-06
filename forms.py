from django import forms

from medical.models import Medicine


class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'
