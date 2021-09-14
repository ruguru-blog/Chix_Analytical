from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, LoginForm
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = LoginForm()
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        # authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("shop:home")
        else:
            messages.info(
                request, f"username or password is incorrect")

    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect('login')


def signup(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Account created successfully for {username}")
            return redirect('login')
    context = {'form': form}
    return render(request, 'signup.html', context)


@login_required(login_url="/accounts/login")
def user_profile(request):
    return render(request, "profile.html")