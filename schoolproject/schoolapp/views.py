from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.shortcuts import render
from .forms import MyForm

# Create your views here.
def home(request):
    return render(request,"home.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/courses')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('login')
    return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpass = request.POST['password1']

        if password == cpass:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=password)

                user.save();
                print("User created")
        else:
            messages.info(request, "Password not matching")
            return redirect('register')
        return redirect('login')
    return render(request, "register.html")

def courses(request):
    return render(request,"courses.html")
def application(request):
    # Initialize the form with department choices
    form = MyForm()
    context = {'form': form}
    if request.method == 'POST':

        messages.success(request, 'Order Confirmed')
        return redirect('application')
    return render(request,"application.html",context)




