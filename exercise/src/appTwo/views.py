from django.shortcuts import render
from django.http import HttpResponse

from .models import TestUser


# Import forms
from .forms import RegisterUserForm, RegisterUserModelForm



def index(request):
    print(request)
    form = RegisterUserForm()

    if request.method == 'POST':
        form = RegisterUserForm(request.POST or None)

        if form.is_valid():
            print("Form is valid")
            print("First Name: "+form.cleaned_data['first_name'])
            print("Last Name: "+form.cleaned_data['last_name'])
            print("Email: "+form.cleaned_data['email'])

    content = "tempor "
    number = 100


    context_dict = {'content': content, 'form': form, 'number': number}
    return render(request, 'apptwo/index.html', context=context_dict)



def users(request):
    users = TestUser.objects.order_by('first_name')

    RegisterForm = RegisterUserModelForm()

    if request.method == 'POST':
        # Meaning some1 has hit submit on the form and is passing information back
        RegisterForm = RegisterUserModelForm(request.POST)

        if RegisterForm.is_valid():
            RegisterForm.save(commit=True)
            return users(request)
        else:
            print("form.errors")


    context_dict = {}
    context_dict['users'] = users
    context_dict['form'] = RegisterForm

    return render(request, 'apptwo/users.html', context_dict)
