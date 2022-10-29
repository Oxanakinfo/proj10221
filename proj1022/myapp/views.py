from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Sheets1022 


def index(request):
    if request.method == 'POST':
        # new_user=Sheets1022(username=request.POST["username"], password=request.POST["password"])
        # new_user = Sheets1022(username = request.POST["username"], password = request.POST["password"])
        new_user = User.objects.create_user(username = request.POST["username"], password = request.POST["password"])
        new_user.save()
        # res = Sheets1022.objects.get()
             # for i in res:
        #     print(i.username)
        #     print(i.password)
        return render(request, "succsess.html")
    else:
        return render(request, "main.html")



def test(request):
    if request.method == "POST":
        new_user = User.objects.create_user(username = request.POST["username"], password = request.POST["password"])
        new_user.save()
        return render(request, "succsess.html")
    else:
        return render(request, "examples.html")


# Create your views here.
