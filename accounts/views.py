from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_http_methods, require_POST

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        name_list = ('양혜빈', '양지은')
        name = request.POST['username']
        if name not in name_list:
            messages.error(request, '가입이 가능한 사용자 이름이 아닙니다.')
            return redirect('accounts:signup')
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
            messages.error(request, '아이디 또는 비밀번호가 다릅니다.')
            return redirect('accounts:login')
    else:
        form = AuthenticationForm(request)
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

@require_GET
@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:article_list')