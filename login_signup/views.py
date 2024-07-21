from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import requests
def home(request):
    return render(request, 'base.html')
def login_page(request):
    if request.method == 'POST':
        form = request.POST
        user = authenticate(username = form['username'], password = form['password'])
        print(user)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, "Invalid Credential")
            return redirect('login')
    return render(request, "login_page.html")

def logout_page(request):
    logout(request)
    return redirect('login')

def signup(request):
    if request.method == "POST":
        form = request.POST
        name = request.POST['fullname']
        try:
            first_name, last_name = name.split()
            first_name = first_name.capitalize()
            last_name = last_name.capitalize()
        except:
            first_name = name.capitalize()
            last_name = " "
        if User.objects.filter(username=form["username"]):
            messages.info(request, "Username Already Exits")
            return redirect('signup')
        user = User.objects.create(first_name = first_name, last_name = last_name, username = form['username'], email = form['email'])
        user.set_password(form['password'])
        user.save()
        messages.info(request, "Registered Successfully !")
        return redirect('login')
    return render(request, "signup.html")
@login_required
def dashboard(request):
    import requests
    url = ('https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=fb3a4616bac24aec9a8958090476cb3d')
    response = requests.get(url)
    content = response.json()['articles']
    print(len(content))
    return render(request, 'dashboard.html', {"f_name": request.user.first_name, "l_name": request.user.last_name, 'all_news' : content})