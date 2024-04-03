from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        
        if User.objects.filter(username=username).exists():
            error_message = 'Username is already taken. Please choose a different one.'
            return render(request, 'signup.html', {'error_message': error_message})

        
        user = User.objects.create_user(username=username, password=password, email=email)
        login(request, user)
        return redirect('success')  
    return render(request, 'signup.html')

def success(request):
    return render(request, 'success.html')

def user_login(request):
    error_message = None  
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  
        else:
            error_message = 'Invalid username or password. Please try again.'

    return render(request, 'login.html', {'error_message': error_message})

def index(request):
    if request.method == "POST":
        text = request.POST.get('words')
        words = str(text).strip()
        number_of_words = len(words.split())

        return render(request, 'index.html', {
            'n_words': number_of_words,
            'words': words,
        })

    return render(request, 'index.html')