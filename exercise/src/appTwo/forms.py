from django import forms
from .models import TestUser

from django.contrib.auth.models import User
from .models import UserProfileInfo


# Using forms.Form
class RegisterUserForm(forms.Form):
    first_name = forms.CharField(max_length=124)
    last_name = forms.CharField(max_length=124)
    email = forms.EmailField()
    botcatcher = forms.CharField(required=False,
                                widget= forms.HiddenInput)

    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError("Bye bot..Gotcha")
        return botcatcher



# Using ModelForm
class RegisterUserModelForm(forms.ModelForm):
    #put custom validations here

    class Meta:
        model = TestUser
        fields = "__all__"



#UserForm
