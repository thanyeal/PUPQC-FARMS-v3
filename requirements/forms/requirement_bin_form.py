from datetime import timezone
from django import forms
from utilities.models import RequirementCategory
from requirements.models import RequirementBin
from django.core.validators import RegexValidator
from django.forms import ValidationError, modelformset_factory


class CreateRequirementBin(forms.ModelForm):
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
    
    deadline = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 
                                                                    'class': 'form-control'}),
                                                                    required=True,
                                                                    error_messages={'required': "Please set the star deadline before submitting the form."})
    
    category = forms.ModelChoiceField(
        label = "Requirement Category", 
        widget=forms.Select(attrs={'class': 'form-control form-select'}), 
        queryset=RequirementCategory.objects.filter(is_deleted=False), 
        required=True, 
        empty_label="Select a Semester",
        error_messages={'required': "Please select a semester before adding a new requirement category."})
    

    
    class Meta:
        model = RequirementBin
        fields = ('name', 'description', 'deadline', 'category')

class EditRequirementBin(forms.ModelForm):
    STATUS_CHOICES = [
            ('ongoing', 'Ongoing'), 
            ('past due', 'Past due'), 
        ]    




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
    
    deadline = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 
                                                                    'class': 'form-control'}),
                                                                    required=True,
                                                                    error_messages={'required': "Please set the star deadline before submitting the form."})
    
    category = forms.ModelChoiceField(
        label = "Requirement Category", 
        widget=forms.Select(attrs={'class': 'form-control'}), 
        queryset=RequirementCategory.objects.filter(is_deleted=False), 
        required=True, 
        empty_label="Select a Semester",
        error_messages={'required': "Please select a semester before adding a new requirement category."})
    


    status = forms.ChoiceField(
        label = "Status", 
        choices = STATUS_CHOICES,
        required = True, 
        error_messages={'required': "Please select a status before submitting the form."},
        widget=forms.Select(attrs={'class': 'form-control form-select select'}))
    

    
    class Meta:
        model = RequirementBin
        fields = ('name', 'description', 'deadline', 'category', 'status')

    





