from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
import requests
def login_view(request):
    if request.user.is_authenticated:
        return redirect('landing_page')

    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            login(request, user)


            trigger_workflow()

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

def trigger_workflow():
    url = "https://automatika.viewdns.net/webhook/f6174d6a-1b24-4e24-9dcf-5a7b30663f30"
    try:
        res = requests.get(url, timeout=10)  
        print("Workflow déclenché :", res.status_code)
    except Exception as e:
        print("Erreur déclenchement workflow :", e)