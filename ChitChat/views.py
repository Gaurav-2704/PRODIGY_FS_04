import contextlib
from contextvars import Token
from django.contrib.auth import logout
from django.shortcuts import render, redirect

def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('login-user')  # Redirect to the named URL pattern 'login-user'
    
    context = {}
    return render(request, "chat/chatPage.html", context)


def logoutView(request):
    logout(request)
    return redirect('login-user')
