from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth import forms
from formtools.wizard.views import SessionWizardView
from pprint import pprint

from .forms import UserCreationForm_1, UserCreationForm_2, AuthenticationForm

class signup(SessionWizardView):
    template_name='accounts/signup.html'
    form_list = [UserCreationForm_1, UserCreationForm_2]
    # GET passes all local variables to the template

    def done(self, form_list, **kwargs):    # works as: after all posts do this

        form_step = [form for form in form_list]

        # step 1: ModelForm
        user = form_step[0].save()
        auth_login( self.request, user )
        # step 2: Form
        user = form_step[1].save()

        return redirect( 'home' )

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm( data=request.POST )
        if form.is_valid():

            user = form.get_user()
            auth_login( request, user )

            return redirect( 'home' )
    else:
        form = AuthenticationForm()
    return render( request, 'accounts/login.html', {'form':form} )

def logout(request):
    auth_logout( request )
    return redirect( 'home' )
