from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import CreateUserForm,UserUpdateForm,ProfileUpdateForm
from django.contrib import messages



def register(request):
    # Check if the request method is POST (form submission)
    if request.method == "POST":
        # Bind the form to the POST data
        form = CreateUserForm(request.POST)
        
        # Check if the form is valid
        if form.is_valid():
            # Save the user registration data to the database
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account has been created for {username} ')
            # Redirect to a success page, e.g., a login page
            return redirect('user-login')  # Replace 'login' with the actual URL name

    # If the request method is GET (display the registration form)
    else:
        # Create a new instance of UserCreationForm
        form = CreateUserForm()

    # Create a context dictionary with the form
    context = {'form': form}

    # Render the registration form template
    return render(request, 'user/register.html', context)

def profile(request):
    return render(request,'user/profile.html')


def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user-profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context ={ 
        'user_form':user_form,
        'profile_form':profile_form,
    }
    return render(request,'user/profile_update.html', context)
