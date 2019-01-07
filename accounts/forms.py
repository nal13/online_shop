#
# ref:
#   https://docs.djangoproject.com/en/2.1/topics/auth/customizing/#a-full-example
# migration problems:
#   https://stackoverflow.com/questions/44651760/django-db-migrations-exceptions-inconsistentmigrationhistory
#

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from phonenumber_field.formfields import PhoneNumberField
from pprint import pprint

from .models import MyUser
from shop.views import add_cliente      # app shop gets forms values from signup


# form wizard
class UserCreationForm_1(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input100', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input100', 'placeholder': 'Repeat Password'}))

    class Meta:
        model = MyUser
        fields = ('shown_name', 'email')
        widgets = {
            'email': forms.EmailInput(attrs={'class':'input100', 'placeholder': 'Email'}),
            'shown_name': forms.TextInput(attrs={'class':'input100', 'placeholder': 'User name'}),
        }

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        pprint( 'saving to DB' )
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserCreationForm_2(forms.Form):
    name = forms.CharField( max_length=40, widget=forms.TextInput(attrs={'class':'input100', 'placeholder': 'Name'}) )
    date_of_birth = forms.DateField( input_formats=('%d/%m/%Y', ), widget=forms.DateInput(format='%d/%m/%Y', attrs={'class':'input100', 'placeholder': 'Date of Birth'}) )
    phone = PhoneNumberField( widget=forms.TextInput(attrs={'class':'input100', 'placeholder': 'Phone'}) )
    address = forms.CharField( widget=forms.TextInput(attrs={'class':'input100', 'placeholder': 'Address'}) )

    def save(self, user):
        pprint( 'saving to somewhere else' )

        forms=self.cleaned_data
        # format fields
        forms['date_of_birth'] = forms['date_of_birth'].strftime('%d/%m/%Y')
        forms['phone'] = str(forms['phone'].national_number)
        # add email field from userModel
        forms.update( {'email':user.email} )
        forms.update( {'codigopostal':'0000-000'} )

        client_id = add_cliente( signup_forms=forms )
        user.set_client_id( client_id )

        return

# extend AuthenticationForm
class AuthenticationForm(AuthenticationForm):
    # the unique Authentication field is email, the form 'username' is the form that corresponds to email
    username = forms.EmailField(widget=forms.EmailInput(attrs={'class':'input100', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input100', 'placeholder': 'Password'}))
