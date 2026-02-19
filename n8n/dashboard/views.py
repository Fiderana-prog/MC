from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
def login_view(request):
    if request.user.is_authenticated:
        return redirect('landing_page')

    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('landing_page')

    return render(request, "register/login.html", {"form": form})

def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html')
def landing_page(request):
    return render(request, 'dashboard/landing_page.html')
def logout_view(request):
    logout(request)
    return redirect('landing_page')
def dashboard(request):
    return render (request, 'dashboard/dashboard.html')