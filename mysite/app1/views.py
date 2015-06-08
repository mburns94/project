from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, User
from django.contrib.auth import authenticate, login


def index(request):
	all_posts = Post.objects.order_by('-likes')[:6]
	args = {'all_posts':all_posts}
	return render(request, 'app1/index.html', args)

def login_user(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                return redirect('/app1/')
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render(request, 'app1/auth.html',{'state':state, 'username': username})
