from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import View
def Home(request):
    x=User.objects.all()
    return render(request,'home.html',{
        'obj':x
    })
