from django.shortcuts import render, render_to_response, redirect
from django.template.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.models import User

from photo.forms import PhotoForm
from photo.models import Photography


def photos(request, user_id=1):
    args = {}
    args.update(csrf(request))
    user = auth.get_user(request)
    if user is not None:
        if user.id is int(user_id):
            args['form'] = PhotoForm
        args['userid'] = user.id
        args['username'] = user.username
    args['photos'] = Photography.objects.filter(photo_user=user_id)
    args['photousername'] = User.objects.get(id=user_id).username
    return render_to_response('photos.html', args)

def photo(request, photo_id=1):
    return render_to_response('photo.html', {'photo': Photography.objects.get(id=photo_id),
                                             'username': auth.get_user(request).username})

def add_photo(request):
    if request.POST:
        form = PhotoForm(request.POST, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.photo_user = auth.get_user(request)
            form.save()
    return redirect('/photos/%s/' %(auth.get_user(request).id))

def all_photos(request):
    args = {}
    args.update(csrf(request))
    user = auth.get_user(request)
    args['userid'] = user.id
    args['username'] = user.username
    args['users'] = User.objects.all()
    args['photos'] = Photography.objects.all()
    return render_to_response('all_photos.html', args)