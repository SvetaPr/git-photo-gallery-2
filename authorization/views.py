from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, render_to_response
from django.template.context_processors import csrf
from django.contrib import auth


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/photos/%s/' %(user.id))
        else:
            args['login_error'] = "There is on such user"
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)

def logout(request):
    auth.logout(request)
    return redirect('/auth/login/')

def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('/photos/%s/' %(newuser.id))
        else:
            args['form'] = newuser_form
    return render_to_response('register.html', args)