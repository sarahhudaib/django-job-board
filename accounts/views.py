from django.shortcuts import redirect, render
from .forms import SignupForm
from django.contrib.auth import authenticate, login
from .models import Profile
# from .models import Profile, UserForm , ProfileForm

from django.urls import reverse


'''
1. It creates a SignupForm object with the POST data passed to the function in the request parameter.
2. It checks if the form is valid by calling the is_valid() method on the form object.
3. If the form is valid, it saves the form data to the database by calling the save() method on the form object.
4. It retrieves the username and password from the form's cleaned_data attribute, which is a dictionary containing the form data that has been "cleaned" and validated.
5. It authenticates the user by calling the authenticate function and passing it the username and password obtained from the form.
6. If the authentication is successful, it logs the user in by calling the login function and passing it the request and user objects.
7. It redirects the user to the '/accounts/profile' URL.

*** If the function is called with a GET request, it simply creates an empty SignupForm object and renders the signup.html template, passing the form object to the template as the form variable.
'''
# Create your views here.
def signup(request):
    # 1. check if the request method is post (there is data & you want to save it)
    if request.method=="POST":
        form = SignupForm(request.POST)
        
        # 2. check if the data is valid the save it 
        if form.is_valid():
            form.save()
            
            # 3. to update the session i need to get the username & the password data
            username = form.cleaned_data['username']  # will give me the username
            password = form.cleaned_data['password1'] # will give me the password 1 or 2 are the same so it doesn't matter which one i chose
            
            # 4. make sure that the data i took exist
            user = authenticate(username=username,password=password)
            
            # 5. if its correct then i need to login
            login(request,user)
            
            # 6. redirect the user to there profile
            return redirect('/accounts/profile')
    
    # 7. check if the user didn't put any data yet the render the form
    else:
        form = SignupForm()
        
    # 8. render the html page
    return render(request,'registration/signup.html',{'form':form})


'''
1. It retrieves the Profile object for the current user by calling the get method on the Profile model's objects attribute and passing it the user field of the request object.
2. It renders the profile.html template and passes the Profile object as the profile variable to the template.
'''
def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{'profile': profile})



def profile_edit(request):
    return render(request,'accounts/profile_edit.html',{})