from django.shortcuts import render,reverse

# Create your views here.

from django.http import HttpResponseRedirect
from django.contrib.auth import logout

def logout_view(request):
    """注销用户"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))