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

- 