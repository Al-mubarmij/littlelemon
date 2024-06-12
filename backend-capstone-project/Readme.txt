
*** note *** 
if you want to see the code
the views, models, serializers, and urls of these are in the restaurant app. 
************


> To check whether the app serves static content with Django:
    - go to -> http://127.0.0.1:8000/restaurant/
    - to see the code, go to the project level's templates/index.html
    - the static files are in restaurant/static/restaurant

> To register a user: 
    - go to http://127.0.0.1:8000/auth/users/
    
> To obtain a Token:
    - go to -> http://127.0.0.1:8000/auth/token/login 
    OR
    - go to -> http://127.0.0.1:8000/restaurant/api-token-auth/ 
      with insomnia using POST and enter username and password in form paramenters

> To check the booking:
    - got to -> http://127.0.0.1:8000/restaurant/booking/
    - login first or use the token.
    - if you aren't logged in you will see: 
        "detail": "Authentication credentials were not provided."

> To check the menu items: 
    - go to -> http://127.0.0.1:8000/restaurant/menu-items/
    - if you aren't logged in you will see: 
        "detail": "Authentication credentials were not provided."
    
> To check a single Menu item: 
    - go to -> http://127.0.0.1:8000/restaurant/menu-items/1
    - if you are logged in or have a token you will be able to  
        view, edit, or delete the item.

> To run the tests
    - in the shell run: python manage.py test 
    - you should get OK
    - *you might get a warning about the datetime
