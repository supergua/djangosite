from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    user_list = User.objects.all()
    return render(request, 'home.html', {'user_list': user_list})
