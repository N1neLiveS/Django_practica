from django import forms

class CSVUploadForm(forms.Form):
    MODEL_CHOICES = [
        ('Graduate', 'Graduate'),
        ('Company', 'Company'),
    ]
    model_name = forms.ChoiceField(choices=MODEL_CHOICES)
    csv_file = forms.FileField()