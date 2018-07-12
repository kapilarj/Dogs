from django.shortcuts import render, redirect
from .models import Dog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import create_dog, RegistrationForm

def user(request):
    return render(request, 'user.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['email']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = RegistrationForm()

    context = {'form' : form}
    return render(request,'registration/register.html',context)

def auth_login(request):
    if request.method == 'POST':
        username = request.POST.get('email_or_contact')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
        return redirect('index')
    else:
        return render(request,'registration/login.html')

def Lout(request):
    logout(request)
    return redirect('/')

def index(request):
    """
    if request.method == 'POST':
        form = create(request.POST)
        if form.is_valid():
            return redirect('/')

    else:
        form = create(request)
    """
    form = create_dog()
    dogs = Dog.objects.all()

    return render(request,'index.html',{'dogs':dogs, 'form':form})



def create(request):
    print(request.POST)
    dog = Dog(name=request.POST.get('name',""), breed=request.POST.get('breed',""))
    dog.save()
    return redirect('/index')


def edit(request, dog_id):
    dog = Dog.objects.get(pk = dog_id)
    context = {"dog":dog}
    return render(request, 'edit.html',context)


def update(request, dog_id):
    dog = Dog.objects.get(pk = dog_id)
    dog.name = request.POST['name']
    dog.breed = request.POST['breed']
    dog.save()
    return redirect('/index')

def delete(request, dog_id):
    Dog.objects.get(pk=dog_id).delete()
    return redirect('/index')

