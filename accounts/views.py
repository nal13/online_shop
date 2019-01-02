from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from pprint import pprint

from .forms import UserCreationForm

def signup( request ):

    pprint( request.POST )

    if request.method == 'POST':
        form = UserCreationForm( request.POST )
        if form.is_valid():

            user = form.save()
            auth_login( request, user )

            return redirect( 'home' )
    else:
        form = UserCreationForm()

    return render( request, 'accounts/signup.html', {'form':form, } )

def login( request ):
    return render( request, 'accounts/login.html' )
