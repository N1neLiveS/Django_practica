from django import forms
from .models import Graduate, EmploymentHistory

class GraduateForm(forms.ModelForm):
    class Meta:
        model = Graduate
        fields = [
            'full_name',
            'date_of_birth',
            'gender',
            'citizenship',
            'address',
            'phone_number',
            'email',
            'snils',
            'study_direction_code',
            'study_direction_name',
            'study_direction_profile',
            'enrollment_year',
            'graduation_year',
            'education_form',
            'employment_book'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }


class HistoryForm(forms.ModelForm):
    class Meta:
        model = EmploymentHistory
        fields = [
            'graduate',
            'employment_placework',
            'employment_status',
            'change_date'
        ]