from django.shortcuts import render, redirect
from . models import FormData

def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        if not name:
            return render(request, 'home.html', {'msg' : 'Please Enter Name', 'submit_flag': False})
        if not email:
            return render(request, 'home.html', {'msg' : 'Please Enter Email', 'name': name, 'submit_flag': False})
        
        if '@' not in email or '.' not in email:
            return render(request, 'home.html', {'msg' : 'Please Enter Valid Email', 'name': name, 'email':email, 'submit_flag': False})
        formData = FormData(name=name, email=email)
        formData.save()
        return render(request, 'home.html', {'msg' : 'Form Submitted successfully.', 'submit_flag': True})
    return render(request, 'home.html')