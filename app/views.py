from django.shortcuts import render
from django.db.models import Count
from django.views import View
from django.views.generic import FormView
from app.models import Product
from app.forms import CustomerRegistrationForm
from django.contrib import messages
class homeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"app\home.html")
    

class CategoryView(View):
    def get(self,request,val) :
        product=Product.objects.filter(category=val)
        title=Product.objects.filter(category=val).values('title')
        return render(request,"app\category.html",{"product":product,"title":title})   
    

class ProductDetailView(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        return render(request,"app/productdetail.html",{"product":product})    

class aboutView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"app/about.html")
class contactView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"app/contact.html")
    

class CustomerRegistrationView(View):
    def get(self,request,*args,**kwargs):
        form= CustomerRegistrationForm() 
        return render(request,"app/registration.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=CustomerRegistrationForm(request.POST) 
        if form.is_valid():
            form.save()
            messages.success(request,"registered successfully")
        else:
            messages.error(request,"invalid input data")    
        return render(request,"app/registration.html",{"form":form})    
    

class SignInView(FormView):
     template_name    
