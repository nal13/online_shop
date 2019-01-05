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
    name = forms.CharField(  max_length=40, widget=forms.TextInput(attrs={'class':'input100', 'placeholder': 'Name'}) )
    date_of_birth = forms.DateField( widget=forms.DateInput(attrs={'class':'input100', 'placeholder': 'Date of Birth'}) )
    phone = PhoneNumberField( widget=forms.TextInput(attrs={'class':'input100', 'placeholder': 'Phone'}) )

    def save(self, commit=True):
        pprint( 'saving to somewhere else' )

        name = self.cleaned_data['name']
        date_of_birth = self.cleaned_data['date_of_birth']
        phone = self.cleaned_data['phone']
        return None

# extend AuthenticationForm
class AuthenticationForm(AuthenticationForm):
    # the unique Authentication field is email, the form 'username' is the form that corresponds to email
    username = forms.EmailField(widget=forms.EmailInput(attrs={'class':'input100', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input100', 'placeholder': 'Password'}))
