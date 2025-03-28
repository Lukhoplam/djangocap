from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
    """
    A form for creating a new user, inheriting from UserCreationForm. This form adds
    an email field, which is required, in addition to the default username and password
    fields.

    Attributes:
        email (forms.EmailField): An email field that is required to be filled.

    Meta:
        model (User): The model associated with this form is the `User` model.
        fields (tuple): The fields included in the form are 'username', 'email',
                        'password1', and 'password2'.

    Methods:
        save(commit=True):
            Saves the form data to create a new user, including the email address,
            and returns the saved user instance. If commit is True, the user is saved
            to the database; otherwise, the user object is returned without saving.
    """
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

