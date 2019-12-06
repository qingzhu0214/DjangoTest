from django.shortcuts import render
from login import models
# Create your views here.

user_list = []
def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        models.UserInfo.objects.create(user=username, pwd = password)

    user_list = models.UserInfo.objects.all()
    return render(request, 'index.html', {'data':user_list})