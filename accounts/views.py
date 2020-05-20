from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required 
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib import messages

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        possible_names = ['양혜빈', '양지은']
        name = request.POST['username'] 
        if name not in possible_names:
            messages.error(request, '가입이 가능한 사용자 이름이 아닙니다.')
            return redirect('accounts:signup')
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:article_list')
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:article_list')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

@require_GET
@login_required
def logout(request):
    auth_logout(request)
    return redirect('accounts:login')
