# your_app/views.py
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from accounts.forms.authentication_forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


def login_user(request):
    if request.method == 'POST':

        form  = AuthenticationForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            print('VALID USER')
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard:dashboard')
        
    else:
        form = AuthenticationForm()

    # str = "gatchalian123"
    # hashed_str = generate_password_hash(str, method='pbkdf2', salt_length=16)

    return render(request, 'authentication/login.html', {'form': form})


@login_required
def logout_user(request):
    auth.logout(request)
    # Redirect to a success page.
    return redirect('login')
