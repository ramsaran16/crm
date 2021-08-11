from django.shortcuts import render,HttpResponse,redirect
from .models import add_form,Item
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
 
@login_required()
def index(request):
    products = Item.objects.all()
    context = {'products':products}
    return render(request, 'placement_view.html', context)

@login_required()
def addProduct(request):
    if request.method == "POST":
        prod = Item()
        prod.name = request.POST.get('name')
        prod.empid = request.POST.get('empid')
        prod.doj = request.POST.get('doj')
        prod.dor = request.POST.get('dor')
        prod.lws = request.POST.get('lws')

        

        prod.save()
        # messages.success(request, "Product Added Successfully")
        return redirect('/')
    return render(request, 'placement.html')

