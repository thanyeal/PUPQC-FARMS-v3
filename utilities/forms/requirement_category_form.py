from datetime import timezone
from django import forms
from utilities.models import RequirementCategory, Semester
from django.core.validators import RegexValidator
from django.forms import ValidationError, modelformset_factory


class CreateRequirementCategory(forms.ModelForm):
    title = forms.CharField(
        label = "Title", 
        required=True, 
        validators= [RegexValidator(r'^[a-zA-ZÁ-ÿ\s.,\'()&0-9\-/\\]*$', 
        message="Only Letters, Numbers, Decimal Point, Comma, Apostrophe, Ampersand, Parentheses, hyphen (-), forward slash (/), and backslash (\) are allowed in the Title Field!")],
        error_messages={'required': "Please enter a title before submitting the form."},
        widget=forms.TextInput(attrs={'class': 'form-control required'}),)
    
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),  # Add the class here
        max_length=2000,
        required=False
        )
    

    semester = forms.ModelChoiceField(
        label = "Semester", 
        widget=forms.Select(attrs={'class': 'form-control form-select'}), 
        queryset=Semester.objects.filter(is_deleted=False, has_child_records = False), 
        required=True, 
        empty_label="Select a Semester",
        error_messages={'required': "Please select a semester before adding a new requirement category."})

    
    class Meta:
        model = RequirementCategory
        fields = ('title', 'description','semester')



class EditRequirementCategory(forms.ModelForm):
    title = forms.CharField(
        label = "Title", 
        required=True, 
        validators= [RegexValidator(r'^[a-zA-ZÁ-ÿ\s.,\'()&0-9\-/\\]*$', 
        message="Only Letters, Numbers, Decimal Point, Comma, Apostrophe, Ampersand, Parentheses, hyphen (-), forward slash (/), and backslash (\) are allowed in the Title Field!")],
        error_messages={'required': "Please enter a title before submitting the form."},
        widget=forms.TextInput(attrs={'class': 'form-control required'}),)
    
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),  # Add the class here
        required=False
        )
    

    semester = forms.ModelChoiceField(
        label = "Semester", 
        widget=forms.Select(attrs={'class': 'form-control form-select'}), 
        queryset=Semester.objects.filter(is_deleted=False), 
        required=True, 
        empty_label="Select a Semester",
        error_messages={'required': "Please select a semester before adding a new requirement category."})

    
    class Meta:
        model = RequirementCategory
        fields = ('title', 'description','semester')

    





