from datetime import timezone
from django import forms
from .models import RequirementCategory, SchoolYear, Semester
from django.core.validators import RegexValidator
from django.forms import ValidationError, modelformset_factory


# class ProgramAccreditation_Form(forms.ModelForm):
#     program = forms.ModelChoiceField(
#         label = "Program", 
#         queryset= Programs.objects.filter(is_deleted=False), 
#         required=True, 
#         empty_label="Select a Program",
#         error_messages={'required': "Please select a level before submitting the form."},
#         widget=forms.Select(attrs={'class': 'form-control form-select select'}))
    
#     instrument_level = forms.ModelChoiceField(
#         label = "Instrument Level", 
#         queryset= instrument_level.objects.filter(is_deleted=False), 
#         required=True, 
#         empty_label="Select an Instrument Level",
#         error_messages={'required': "Please select an Instrument Level before submitting the form."},
#         widget=forms.Select(attrs={'class': 'form-control form-select select'}))
    
#     mock_accred_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 
#                                                                      'class': 'form-control'}),
#                                                                        required=True,
#                                                                         error_messages={'required': "Please set the mock accreditation date beefore submitting the form."})
    
    
#     survey_visit_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 
#                                                                      'class': 'form-control'}), 
#                                                                      required=True,
#                                                                       error_messages={'required': "Please set the survey visit date before submitting the form."})

#     class Meta:
#         model = program_accreditation
#         fields = ('program', 'instrument_level', 'mock_accred_date', 'survey_visit_date', 'description')

#         widgets = {
#             'description': forms.Textarea(attrs={'required': False, 'class': 'form-control'}),
#         }

#     def clean(self):
#         cleaned_data = super().clean()
#         mock_accred_date = cleaned_data.get('mock_accred_date')
#         survey_visit_date = cleaned_data.get('survey_visit_date')

#         if not survey_visit_date:
#             raise ValidationError("Please set the survey visit date before submitting the form. ")

#         if mock_accred_date and survey_visit_date:
#             # Check if mock_accred_date is equal to survey_visit_date
#             if mock_accred_date == survey_visit_date:
#                 raise ValidationError("Mock Accreditation Date cannot be equal to the survey visit date. ")

#             # Check if mock_accred_date is after survey_visit_date
#             if mock_accred_date > survey_visit_date:
#                 raise ValidationError("Mock Accreditation Date cannot be after the survey visit date. ")

#             # Check if mock_accred_date is before the current date
#             if mock_accred_date < timezone.now():
#                 raise ValidationError("Mock Accreditation Date should be set in the future. ")

#         return cleaned_data





class CreateSchoolYear(forms.ModelForm):
    name = forms.CharField(
        label = "Name", 
        required=True, 
        validators= [RegexValidator(r'^[a-zA-ZÁ-ÿ\s.,\'()&0-9\-/\\]*$', 
        message="Only Letters, Numbers, Decimal Point, Comma, Apostrophe, Ampersand, Parentheses, hyphen (-), forward slash (/), and backslash (\) are allowed in the Name Field!")],
        error_messages={'required': "Please enter a name before submitting the form."},
        widget=forms.TextInput(attrs={'class': 'form-control required'}),)
    
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 
                                                                     'class': 'form-control'}),
                                                                       required=True,
                                                                        error_messages={'required': "Please set the star date before submitting the form."})
    
    
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 
                                                                     'class': 'form-control'}), 
                                                                     required=True,
                                                                      error_messages={'required': "Please set the end date before submitting the form."})


    class Meta:
        model = SchoolYear
        fields = ('name', 'start_date', 'end_date')


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
        widget=forms.Select(attrs={'class': 'form-control'}), 
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
    


class CreateRequirementCategory(forms.ModelForm):
    title = forms.CharField(
        label = "Title", 
        required=True, 
        validators= [RegexValidator(r'^[a-zA-ZÁ-ÿ\s.,\'()&0-9\-/\\]*$', 
        message="Only Letters, Numbers, Decimal Point, Comma, Apostrophe, Ampersand, Parentheses, hyphen (-), forward slash (/), and backslash (\) are allowed in the Title Field!")],
        error_messages={'required': "Please enter a title before submitting the form."},
        widget=forms.TextInput(attrs={'class': 'form-control required'}),)
    
    description = forms.CharField(widget=forms.Textarea(attrs={}), max_length=2000,  required=False)
    

    school_year = forms.ModelChoiceField(
        label = "School Year", 
        widget=forms.Select(attrs={'class': 'form-control'}), 
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
        model = RequirementCategory
        fields = ('title', 'description','semester')


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
    





