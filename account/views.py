from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Profile
from rest_framework import generics, authentication, permissions
from .serializers import UserSerializer, TokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer

class ManageUserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user



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


class TokenCreateView(ObtainAuthToken):
    serializer_class = TokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES



    



