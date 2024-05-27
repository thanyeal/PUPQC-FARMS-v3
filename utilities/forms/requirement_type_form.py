from datetime import timezone
from django import forms
from utilities.models import RequirementCategory, RequirementType, Semester
from django.core.validators import RegexValidator
from django.forms import ValidationError, modelformset_factory


class CreateRequirementType(forms.ModelForm):
    name = forms.CharField(
        label = "Name", 
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
    

    
    class Meta:
        model = RequirementType
        fields = ('name', 'description')

class EditRequirementType(forms.ModelForm):
    name = forms.CharField(
        label = "Name", 
        required=True, 
        validators= [RegexValidator(r'^[a-zA-ZÁ-ÿ\s.,\'()&0-9\-/\\]*$', 
        message="Only Letters, Numbers, Decimal Point, Comma, Apostrophe, Ampersand, Parentheses, hyphen (-), forward slash (/), and backslash (\) are allowed in the Name Field!")],
        error_messages={'required': "Please enter a Name before submitting the form."},
        widget=forms.TextInput(attrs={'class': 'form-control required'}),)
    
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),  # Add the class here
        required=False
        )
    

    
    class Meta:
        model = RequirementType
        fields = ('name', 'description')

    





