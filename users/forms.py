from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import BooleanField
from users.models import User
from django import forms

from django.forms import ImageField, FileInput
class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

class UserProfileForm(StyleFormMixin, UserChangeForm):
    avatar = ImageField(widget=FileInput)

    class Meta:
        model = User
        fields = ('phone', 'avatar', 'city')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()

class RecoverPasswordForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)