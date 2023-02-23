from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render


@login_required
def profile(request):
    if request.method == 'GET':
        user = request.user
        return render(request, 'accounts/profile.html', {})

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            login(request, form)
            return redirect('products:home')
    return render(request, 'accounts/register.html', {'form': form})

def logout(request):
    logout(request)
    return redirect('products:home')

class Login(LoginView):
    template_name = 'accounts/login.html'