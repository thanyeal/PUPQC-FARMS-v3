from django import forms
from accounts.models import FISFaculty, FARMSUser  # Replace 'other_app' with your actual app name
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

class AuthenticationForm(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:

            try:
                user = FISFaculty.objects.get(Email=email)
                if not check_password_hash(user.Password, password):  # Assuming you have check_password method in FISFaculty
                            raise forms.ValidationError("Invalid email or password")
            except FISFaculty.DoesNotExist:
                try:
                    user = FARMSUser.objects.get(Email=email)

                    if not check_password_hash(user.password, password):  # Assuming you have check_password method in FISFaculty
                        raise forms.ValidationError("Invalid email or password")
                except FARMSUser.DoesNotExist:
                    raise forms.ValidationError("Invalid email or password")

            
        return cleaned_data
