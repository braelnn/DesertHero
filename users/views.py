from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CustomAuthenticationForm
from django.core.mail import send_mail
import random

# View for login
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Authenticate user
            user = authenticate(request, username=username, password=password)
            if user is not None and user.email == email:
                login(request, user)

                # Generate and send verification code
                verification_code = random.randint(100000, 999999)
                request.session['verification_code'] = verification_code

                send_mail(
                    'Your Verification Code',
                    f'Your verification code is: {verification_code}',
                    'blessingbraelly@gmail.com',  # Use your email address here
                    [user.email],
                    fail_silently=False,
                )

                # Redirect to the verification page
                return redirect('users:verify_code')

            else:
                messages.error(request, 'Invalid credentials or email.')

        else:
            messages.error(request, 'Form is not valid. Please check your credentials.')

    form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})


# View for code verification
def verify_code_view(request):
    if request.method == 'POST':
        entered_code = request.POST.get('verification_code')

        if entered_code == str(request.session.get('verification_code')):
            user = request.user

            # Logic to check the email and show the modal
            if user.email == 'kalakoalice45@gmail.com':
                # Set the flag to show the modal for 'kalakoalice45@gmail.com'
                request.session['show_dashboard_modal'] = True
                return render(request, 'verify_code.html', {'show_modal': True})

            else:
                # Redirect to dashboard 1 after verification for any other email
                return redirect('users:dashboard1')

        else:
            messages.error(request, 'Invalid verification code.')

    return render(request, 'verify_code.html', {'show_modal': False})

# Dashboard 1 view
def dashboard1_view(request):
    return render(request, 'dashboard1.html')


# Dashboard 2 view
def dashboard2_view(request):
    return render(request, 'dashboard2.html')
