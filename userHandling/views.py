from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from carthagoHome import urls
from userHandling.forms import UserForm, UserProfileInfoForm
from userHandling.models import UserProfile

# Create your views here.
def index(request):
    return render(request, 'userHandling/index.html')

#Allow user to logout. Decorator must be above action.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('carthago-home'))


def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'image' in request.FILES:
                profile.image = request.FILES['image']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'userHandling/registration.html',
                            {'user_form':user_form,
                            'profile_form':profile_form, 'registered':registered})





def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                # If user has a successful login then we can forward them to another page.
                login(request, user)
                return HttpResponseRedirect(reverse('carthago-home'))

            else:
                return HttpResponse("Account not found. Please sign up.")
        else:
            print("Someone tried to login and failed.")
            print("Username: {}  and password {}".format(username,password))
            return HttpResponse("Invalid login details given.")
    else:
        return render(request, 'userHandling/login.html')



def profile(request):
    return render(request, 'userHandling/profile.html')
