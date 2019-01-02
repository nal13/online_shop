#
# ref:
#   https://docs.djangoproject.com/en/2.1/topics/auth/customizing/#a-full-example
# migration problems:
#   https://stackoverflow.com/questions/44651760/django-db-migrations-exceptions-inconsistentmigrationhistory
#

from django import forms

from .models import MyUser

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'input100', 'placeholder': 'Password'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class':'input100', 'placeholder': 'Repeat Password'}))

    class Meta:
        model = MyUser
        fields = ('email', 'date_of_birth')
        widgets = {
            'email': forms.EmailInput(attrs={'class':'input100', 'placeholder': 'Email'}),
            'date_of_birth': forms.DateInput(attrs={'class':'input100', 'placeholder': 'Date of Birth'}),
        }

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
