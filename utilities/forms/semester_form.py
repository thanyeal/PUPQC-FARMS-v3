from datetime import timezone
from django import forms
from utilities.models import SchoolYear, Semester
from django.core.validators import RegexValidator
from django.forms import ValidationError, modelformset_factory


class CreateSemester(forms.ModelForm):
    name = forms.CharField(
        label = "Name", 
        required=True, 
        validators= [RegexValidator(r'^[a-zA-ZÁ-ÿ\s.,\'()&0-9\-/\\]*$', 
        message="Only Letters, Numbers, Decimal Point, Comma, Apostrophe, Ampersand, Parentheses, hyphen (-), forward slash (/), and backslash (\) are allowed in the Name Field!")],
        error_messages={'required': "Please enter a name before submitting the form."},
        widget=forms.TextInput(attrs={'class': 'form-control required'}),)
    

    school_year = forms.ModelChoiceField(
        label = "School Year", 
        widget=forms.Select(attrs={'class': 'form-control form-select'}), 
        queryset=SchoolYear.objects.filter(is_deleted=False), 
        required=True, 
        empty_label="Select a School Year",
        error_messages={'required': "Please select a school year before adding a new semester."})

    
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 
                                                                     'class': 'form-control'}),
                                                                       required=True,
                                                                        error_messages={'required': "Please set the star date before submitting the form."})
    
    
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 
                                                                     'class': 'form-control'}), 
                                                                     required=True,
                                                                      error_messages={'required': "Please set the end date before submitting the form."})


    class Meta:
        model = Semester
        fields = ('name', 'start_date', 'end_date', 'school_year')


    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if not end_date:
            raise ValidationError("Please set the end date before submitting the form. ")

        if start_date and end_date:
            # Check if start_date is equal to end_date
            if start_date == end_date:
                raise ValidationError("Start date cannot be equal to the end date. ")

            # Check if start_date is after end_date
            if start_date > end_date:
                raise ValidationError("Start date cannot be after the end date. ")

        return cleaned_data
    
    




