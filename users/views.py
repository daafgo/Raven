
from django.shortcuts import redirect, render
from users.forms import RegistrationForm
from users.models import CustomUser

def UserReg(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():

            name_user = form.cleaned_data['username']
            email_user = form.cleaned_data['email']
            pass_user = form.cleaned_data['password1']
            pseudo_ = form.cleaned_data['pseudo']
            create_user = CustomUser.objects.create_user(username = name_user, email = email_user, password = pass_user, pseudo=pseudo_ )
            create_user.save()
            return redirect('/login')

    form = RegistrationForm()
    return render(request,'users/user_form.html', {'title':'Registro', 'form': form})


