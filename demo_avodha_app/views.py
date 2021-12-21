from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from.models import shop
from.import views
from.form import Modelform


# Create your views here.
def demo(request):
    product=shop.objects.all()
    return render(request,"home.html",{'products':product})
def detail(request,shop_id):
    product1=shop.objects.get(id=shop_id)
    return render(request,"detail.html",{'product':product1})
def add_product(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        price = request.POST.get('price')
        img = request.FILES['img']

        s=shop(name=name,desc=desc,price=price,img=img)
        s.save()
        print("product added")
    return render(request,"add_products.html")
def update(request,id):
    obj=shop.objects.get(id=id)
    form=Modelform(request.POST or None,request.FILES,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"edit.html",{'form':form,'obj':obj})
def delete(request,id):
    if request.method == 'POST':
        obj=shop.objects.get(id=id)
        obj.delete()
        return redirect('/')
    return render(request,'delete.html')



