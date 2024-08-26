from django import forms
from .models import CSVFile

class CSVFileForm(forms.ModelForm):
    class Meta:
        model = CSVFile  # This form is tied to the CSVFile model
        fields = ['file']  # This form will have a single field for the file upload