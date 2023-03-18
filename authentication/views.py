from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.views import View
from authentication.models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')



class Login(View):
    def get(self,request):
        return HttpResponse("Loginpage")     

    def post(self,request):
        username=request.POST['username']
        password=request.POST['password']

        if request.user.is_authenticated:
            return HttpResponse(success=True)
        else:
            if username and password:
                user=auth.authenticate(username=username,password=password)
                if user:
                    if user.is_active:
                        if user.is_superuser:
                            auth.login(request,user)
                            return HttpResponse("ADMIN LOGIN")
                        else:
                            auth.login(request,user)
                            c=request.user.id
                            if students.objects.filter(student_username=c).exists():
                                return HttpResponse(success=True)
                            # elif staffs.objects.filter(staff_username=c).exists():
                            #     return redirect('/')
                        
                  
                    return HttpResponse(success=False)
           
                return HttpResponse(success=False)
          
            return HttpResponse(success=False)