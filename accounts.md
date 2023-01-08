# Django Job Board Accounts Managing

## There is two documentation for this feature that can help:
-  [Django Docs](https://docs.djangoproject.com/en/4.1/topics/auth/)
- [MDN Docs](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication)

I prefer MDN docs because they explained the user authentication and permeations in details.

## Now how to create the user authentication STEPS:
- add the accounts path in the project urls
    ```
    path('accounts/', include('django.contrib.auth.urls')),
    ```

    Using the above method adds the following URLs with names in square brackets, which can be used to reverse the URL mappings.

    ```
    accounts/ login/ [name='login']
    accounts/ logout/ [name='logout']
    accounts/ password_change/ [name='password_change']
    accounts/ password_change/done/ [name='password_change_done']
    accounts/ password_reset/ [name='password_reset']
    accounts/ password_reset/done/ [name='password_reset_done']
    accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
    accounts/ reset/done/ [name='password_reset_complete']
    ```

## How Did i generate the EMAIL_HOST_PASSWORD:
you need to know its not your gmail usual password theres a few easy steps to generate it 

1. open your `Gmail` or your `Google Account` 
2. go to --> `Manage your Google Account`
3. from the left bar choose --> `Security` 
4. make sure that your `2-Steps Verification` is on
5. choose --> `App passwords`
6. you will find an empty form select app from the "`Select app`" --> choose `Mail`
7. Now --> `Select device` ---> choose `Other` 
8. Type a `Name` --> i chose my project name "`JobBoard`"
9. Press `Generate` 
10. Copy the `generated key`
11. Press `Done`
12. Paste it here in the setting like this:
`MAIL_HOST_PASSWORD` = `'kcpnwirvkmagqrlr'`

13. or you can hide it in the `.env` file 

----------------------------------------------------------------

## How to create .env file in Django?

To use a .env file with Django, you will need to install the python-dotenv package:

1. `pip install python-dotenv`
2. Then, create a `.env` file in the root of your Django project, and add your email password like this:
    ```
    EMAIL_PASSWORD='kcpnwirvkmagqrlr'
    ```
    you can add also the `EMAIL_HOST_USER` & the `SECRET_KEY`

3. Next, add the following code to the top of your Django settings file to load the values from the `.env` file:

    ```
    import os
    from dotenv import load_dotenv

    load_dotenv()

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = os.getenv('EMAIL_ADDRESS')
    EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD')
    EMAIL_USE_TLS = True
    EMAIL_PORT = '587'
    ```


    -----------
## CSRF error

- To fix the CSRF error I'm encountering, you need to make sure that the csrf_token template tag is included in your HTML form, like this:

```
<form class="form-contact contact_form" method="post" >
            {% csrf_token %}
            <!-- form fields go here -->
</form>
```

This will include a CSRF token in the form, which Django will check when the form is submitted. If the token is not present or is incorrect, Django will return a 403 error.

- In addition, make sure that your view function passes the request object to the template's render method, like this:

```
def send_message(request):
    myinfo = Info.objects.first()

    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            subject,
            message,
            email,
            [settings.EMAIL_HOST_USER],
        )

    return render(request,'contact.html',{'myinfo':myinfo})
```

- Finally, make sure that your browser is accepting cookies. If cookies are disabled, the CSRF token will not be sent with the form submission, and Django will return a 403 error.


----
## `Confirm Form Resubmission` error

This error occurs when a form is submitted, and the user tries to refresh the page or navigate back to the page using the browser's back button.

- Use the `HttpResponseRedirect` function to redirect the user to a different page after the form is submitted. This will prevent the user from resubmitting the form if they refresh the page or navigate back to it:

```
from django.shortcuts import render, HttpResponseRedirect

def send_message(request):
    if request.method == 'POST':
        # process the form
        return HttpResponseRedirect('/success/')
    else:
        return render(request, 'contact.html')
```