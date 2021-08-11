from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm
from .models import TODO
# Create your views here.
def signupuser(request):

    if request.method == 'GET':

        dict_to_pass = {'form': UserCreationForm(),
                       }
        return render(request, 'todolist\sigupuser.html', dict_to_pass)

    else:

        if request.POST['password1'] == request.POST['password2']:
            try:
                new_user=User.objects.create_user(request.POST['username'], password= request.POST['password1'])
                new_user.save()
                login(request,new_user)
                return redirect('welcome')

            except IntegrityError:
                dict_to_pass = {'form': UserCreationForm(),
                                'error': 'Username not available'
                               }
                return render(request, 'todolist\sigupuser.html', dict_to_pass)
        else:
            dict_to_pass = {'form': UserCreationForm(),
                            'error': '!! Passwords did not match !!'
                           }
            return render(request, 'todolist\sigupuser.html', dict_to_pass)
            #inform user passwords didnt match

def welcome(request):
    todos = TODO.objects.filter(user=request.user, completed__isnull=True)
    dict_to_pass={'todos':todos}
    return render(request, 'todolist/welcome.html',dict_to_pass)

def logoutuser(request):
    if request.method == 'POST':

        logout(request)
        dict_to_pass={}
        return redirect('home')
        # return render(request, 'todolist/logout.html',dict_to_pass)

def home(request):
    return render(request, 'todolist/home.html')

def loginuser(request):
    if request.method == 'GET':
        dict_to_pass = {'form': AuthenticationForm()}
        return render(request, 'todolist\login.html', dict_to_pass)

    elif request.method == 'POST':
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            dict_to_pass = {'form': AuthenticationForm(),
                            'error': 'Usernsme and password did not match'
                           }
            return render(request, 'todolist\login.html', dict_to_pass)
        else:
            login(request,

            user)
            return redirect('welcome')




    return render(request, 'todolist/login.html')

def createtodo(request):
    if request.method == 'GET':
        dict_to_pass={'form': TodoForm()}
        return render(request, 'todolist/createtodo.html',dict_to_pass)
    elif request.method == 'POST':
        try :
            form = TodoForm(request.POST)
            new_todo = form.save(commit=False)
            new_todo.user = request.user
            new_todo.save()
            # dict_to_pass = {}
            # return render(request, 'todolist/welcome.html', dict_to_pass)
            return redirect('welcome')
        except ValueError:
            dict_to_pass = {'form': TodoForm(),
                            'error': f"Bad data entered. Try again {request.user}."}
            return render(request, 'todolist/createtodo.html',dict_to_pass)
