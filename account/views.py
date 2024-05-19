from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Profile


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return redirect('account:login')
    else:
        form = RegisterForm()
    return render(request, 'account/register.html', {'form':form})




    



