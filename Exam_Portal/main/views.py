from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
def index(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            
            if user.is_superuser or user.is_staff:
                return redirect('/admin')
            
            if user.groups.filter(name='Professor').exists():
                return redirect('prof:index')
            
            return redirect('student:index')
            

        return render(request, 'main/login.html', { 'wrong_cred_message': 'Error' })

    return render(request, 'main/login.html')


def logoutUser(request):
    logout(request)
    return render(request, 'main/logout.html',{ 'logout_message': 'Logged out Successfully' })

@csrf_exempt
def verify(request):
    if request.method == "POST":
        data = json.loads(request.body)
            
            # Extract specific data from the JSON (e.g., username and password)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if not user.is_superuser or not user.is_staff or not user.groups.filter(name='Professor').exists():
            response_data={'verify':1}
            return JsonResponse(response_data, status=200)
        else:
            response_data={'verify':0}
            return JsonResponse(response_data, status=300)

def get_end(request):
    response_data={'verify':1}
    return JsonResponse(response_data, status=100)
            