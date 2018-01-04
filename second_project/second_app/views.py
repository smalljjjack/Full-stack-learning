from django.shortcuts import render
from django.http import HttpResponse
from second_app.models import Webpage, Topic, AccessRecord, UserProfileInfo#, User
from second_app.forms import UserForm, UserProfileInfoForm
#from second_app.forms import NewUser

#import for login function
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

def base(request):
    return render(request, 'second_app/base.html')

def base2(request):
    context_dict = {'text':'hello world','number':100}
    return render(request, 'second_app/base2.html', context_dict)

def other(request):
    return render(request, 'second_app/other.html')

def relative(request):
    return render(request, 'second_app/relative.html')

'''
def user_register(request):
    print(request)
    form = NewUser()
    if request.method == "POST":
        form = NewUser(request.POST)
        if form.is_valid():
            form.save(commit = True)
            print("Saving!")
            return home(request)
        else:
            print('Error FROM INVALID')
    else:
        print('Error FROM create')
    return render(request, 'second_app/user_register.html', {'form':form})
'''
def home(request):
    return render(request, 'second_app/home.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            # Do something process data
            print("VALIDATION SUCCESS!")
            print("name: " + form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['Email'])
            print("Text: "+form.cleaned_data['text'])
    return render(request, 'second_app/form_page.html', {'form':form})

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {"access_records":webpages_list}
    return render(request,'second_app/index2.html',date_dict)
# Create your views here.

def hello(request):
    return HttpResponse("<em>hello world!</em>")

def second_index(request):
    return render(request, 'second_app/second_index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in, Welcome!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('second_app/second_index')
'''
def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # django aotumatically verify user
        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('second_index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            return HttpResponse("Please check you username and password")
    else:
        return render(request, "second_app/user_login.html")
'''
def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(('second_app/second_index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'second_app/user_login.html', {})

def second_base(request):
    return render(request, 'second_app/second_base.html')

def second_register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit = False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'second_app/second_register.html',
            {'user_form':user_form,
            'profile_form':profile_form,
            'registered':registered})

'''
def users(request):
    users_list = User.objects.order_by('FName')
    user_dict = {"user_records":users_list}
    return render(request,'second_app/User.html',user_dict)

        user_list = User.objects.order_by('first_name')
        user_dict = {"users":user_list}
        return render(request,'apptwo/users.html',context=user_dict)
'''
