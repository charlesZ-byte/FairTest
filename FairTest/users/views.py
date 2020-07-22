from django.shortcuts import render, HttpResponse
import json
from .models import User
# Create your views here.
def loginAuth(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(email=email).exists():
            if User.objects.get(email = email).password == password:
                return HttpResponse(json.dumps({'msg':'good email good password'}), content_type="application/json")
            return HttpResponse(json.dumps({'msg':'good email bad password'}), content_type="application/json")
        return HttpResponse(json.dumps({'msg':'bad email'}), content_type="application/json")
    return render(request, 'login.html')
