from django.shortcuts import render,HttpResponse,redirect
from .models import add_form
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
#login_url='/crm/login'
@login_required()
def example(request):
    return render(request,'home.html')


# Create your views here.
@login_required()
def add_formView(request):
    if request.method == "POST":
        add_form_data=add_form()
        add_form_data.name=request.POST.get('name')
        add_form_data.email=request.POST.get('email')
        add_form_data.phone=request.POST.get('phone')
        add_form_data.yop=request.POST.get('yop')
        add_form_data.degree=request.POST.get('degree')
        add_form_data.status=request.POST.get('status')  
        add_form_data.save()
        messages.success(request, 'successfully') 
        return redirect('/')     
    return render(request,"add_form.html")
@login_required()
def view_data(request):
     std_data =add_form.objects.all()
     
     return render(request,'view_data.html',{'std_data':std_data})
