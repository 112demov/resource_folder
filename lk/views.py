from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.views.generic import ListView, DetailView

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Complete!')
            return redirect('login')
        else:
            messages.error(request, f'ERROR!')
            
    else:
        form = UserRegisterForm()
    return render(request, 'lk/singup.html', {'form': form})
    
    
class UserLoginView(LoginView):
    template_name = 'lk/login.html'
    
    
class UserLogoutView(LogoutView):
    template_name = 'lk/logout.html'
    
@login_required   
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Ваш профиль успешно обновлен.')
            return redirect('home')
            
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    
    return render(request, 'lk/profile.html', context)


class ProfileList(ListView):
    paginate_by = 6
    model = Profile
    template_name = 'lk/list_user.html'
    
    
class ProfileDetail(DetailView):
    model = Profile
    template_name = 'lk/detail_user.html'
    