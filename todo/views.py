import re
from todo.models import Todos
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from django.core.paginator import Paginator

def email_check(user):
    return (user.email.startswith('megan') | user.email.startswith('andres'))

def purchasing_check(user):
    return user.email.startswith('andres')

# Create your views here.

def home(request):
    return render (request, 'todo/home.html')    

def noResults(request):
    return render (request, 'todo/noResults.html')  

def signupuser(request):

    if request.method == 'GET':
        return render (request, 'todo/signupuser.html', {'form':UserCreationForm()})
    else:
        # Create User
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],request.POST['password1'], request.POST['password2'])
                user.save()
                login(request, user)
                return redirect('home')


            except IntegrityError:
                return render (request, 'todo/signupuser.html', {'form':UserCreationForm(), 'error': 'Username is already used, choose another one'})
        else:
            # Tell user password need to match
            print('pass done match')
            return render (request, 'todo/signupuser.html', {'form':UserCreationForm(), 'error': 'Passwords do not match'})

@login_required
def currenttodos(request):
    todos = Todos.objects.filter(user = request.user, datecompleted__isnull =True).order_by('duedate')

    return render(request, 'todo/currenttodos.html', {'todos': todos})

@login_required
def logoutuser(request):
    if request.method =='POST':
        logout(request)
        return redirect('home')

def loginuser(request):
    if request.method == 'GET':
        return render (request, 'todo/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username = request.POST['username'], password= request.POST['password'])
        if user is None:
            return render (request, 'todo/loginuser.html', {'form':AuthenticationForm(), 'error': 'Username and password did not match'})
        else:
            login(request, user)
            return redirect('home')

@login_required       
def createtodo(request):
    if request.method == 'GET':
        return render (request, 'todo/createtodo.html', {'form': TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            newtodo =form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('currenttodos')
        except ValueError:
            return render (request, 'todo/createtodo.html', {'form': TodoForm(), 'error': 'One or more fields has bad data'})

@login_required
def viewtodo(request, todo_pk):
    todo = get_object_or_404(Todos, pk =todo_pk)
    user = get_object_or_404(User, username = todo.user)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request, 'todo/viewtodo.html', {'todo': todo, 'form': form})
    else:
        try:
            form = TodoForm(request.POST, instance =todo)
            form.save()
            
            return redirect('currenttodos')
        except ValueError:

            return render(request, 'todo/viewtodo.html', {'todo': todo, 'form': form, 'error': 'One or more fields has bad data', 'user':user})
@login_required
def completetodo(request, todo_pk):
    todo = get_object_or_404(Todos, pk =todo_pk, user=request.user)
    if request.method == 'POST':
        todo.datecompleted = timezone.now()
        todo.save()
        return redirect('currenttodos')

@login_required
def deletetodo(request, todo_pk):
    todo = get_object_or_404(Todos, pk =todo_pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('currenttodos')

@login_required
def completedtodos(request):
    todos = Todos.objects.filter(user = request.user, datecompleted__isnull =False).order_by('-datecompleted')
    paginator = Paginator(todos,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'todo/completedtodos.html', {'page_obj':page_obj})

@login_required
def reviserequest(request,todo_pk):
    todo = get_object_or_404(Todos, pk =todo_pk)
 
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        
        return render(request, 'todo/viewtodo.html', {'todo': todo, 'form': form})
    else:
        try:
            form = TodoForm(request.POST,  instance=todo)
 
            form.save()
                        
            return redirect('currenttodos')
        except ValueError:

            return render(request, 'todo/viewtodo.html', {'todo': todo, 'form': form, 'error': 'One or more fields has bad data'})
    # if request.method == 'POST':
    #     form = TodoForm(request.POST, instance=todo)
    #     form.save()
    #     return redirect('currenttodos')

@login_required
@user_passes_test(email_check, login_url='/login/')
def billingList(request):
    todos = Todos.objects.filter(tobill =True, billed=False, datecompleted__isnull =False).order_by('duedate')
    paginator = Paginator(todos,4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'todo/billingList.html', {'page_obj': page_obj})

@login_required
def markbilled(request, todo_pk):
    todo = get_object_or_404(Todos, pk =todo_pk)
    if request.method == 'POST':
        todo.billed = True
        todo.save()
        return redirect('billingList')

@login_required
@user_passes_test(purchasing_check, login_url='/login/')
def toOrderList(request):
    todos = Todos.objects.filter(datecompleted__isnull =True).order_by('duedate')
    paginator = Paginator(todos,4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'todo/toOrderList.html', {'page_obj': page_obj})

@login_required
@user_passes_test(purchasing_check, login_url='/login/')
def markordered(request, todo_pk):
    todo = get_object_or_404(Todos, pk =todo_pk)
    if request.method == 'POST':
        if request.POST.get('amount') is not None and request.POST.get('amount') !='':
            todo.datecompleted = timezone.now()
            todo.rush = False
            todo.amount = request.POST.get("amount")
            todo.save()
            return redirect('toOrderList')
        else:
            todo.datecompleted = timezone.now()
            todo.rush = False
            todo.amount = 0.00
            todo.save()
            return redirect('toOrderList')

@login_required
@user_passes_test(purchasing_check, login_url='/login/')
def orderedList(request):
    todos = Todos.objects.filter(datecompleted__isnull =False).order_by('-datecompleted')
    paginator = Paginator(todos,4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'todo/orderedList.html', {'page_obj': page_obj})

@login_required
@user_passes_test(email_check, login_url='/login/')
def billedcomplete(request):
    todos = Todos.objects.filter(billed=True).order_by('-datecompleted')
    paginator = Paginator(todos,12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'todo/completedBillings.html', {'page_obj': page_obj})


@login_required
def seach_results(request):
    query = request.GET.get('q')
    todos = Todos.objects.filter(Q(part__icontains=query) | Q(description__icontains=query), datecompleted__isnull=False).order_by('-datecompleted')
    
    if todos.count() == 0:
        return redirect('no_results')
    else:
        paginator = Paginator(todos,4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        return render(request, 'todo/searchResults.html', {'page_obj': page_obj, 'query':query})

@login_required
def repeat_request(request, todo_pk):
    todo = get_object_or_404(Todos, pk =todo_pk)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request, 'todo/repeatRequest.html', {'todo': todo, 'form': form})
    else:
        try:
            form = TodoForm(request.POST)
            newtodo =form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('currenttodos')
        except ValueError:
            return render (request, 'todo/repeatRequest.html', {'form': TodoForm(), 'error': 'One or more fields has bad data'})
