from django.shortcuts import render,redirect
from .models import Crudapp
from django.contrib import messages

# Create your views here.

def crude(request):
    return render(request,'crude.html')

def add_data(request):
    return render(request,'add_data.html')

def views_records(request):
    all_datas=Crudapp.objects.all()
    return render(request,'views_record.html',{'datass':all_datas})

def registation(request):
    if request.method=='POST':
        name = request.POST['name']
        fname=request.POST['father']
        mname=request.POST['mother']
        email=request.POST['email']
        phone=request.POST['phone']
        address=request.POST['address']
        images=request.FILES['images']
        data=Crudapp(name=name, father=fname,mother=mname,email=email,phone=phone,address=address,images=images)
        data.save()
        messages.success(request, 'Your data was submitted successfully!')
    
        return redirect('/add_data/')
    else:
        messages.error(request, 'Something went wrong. Please try again.')
        return redirect('/add_data/')
    
def delete(request,id):
    delet=Crudapp.objects.get(id=id)
    delet.delete()
    messages.error(request, 'data has been delete successfully.')
    return redirect('/views_records/')

def update(request,id):
    datass=Crudapp.objects.get(id=id)
    return render(request,'update_data.html',{'stores':datass})

def edite(request,id):
    name=request.POST['name']
    father=request.POST['father']
    mother=request.POST['mother']
    email=request.POST['email']
    phone=request.POST['phone']
    address=request.POST['address']
    images=request.FILES['images']
    updatedata=Crudapp.objects.get(id=id)
    updatedata.name=name
    updatedata.father=father
    updatedata.mother=mother
    updatedata.email=email
    updatedata.phone=phone
    updatedata.address=address
    updatedata.images=images
    updatedata.save()
    messages.success(request, 'Your data was update successfully!')
    return redirect('/views_records/')

def report(request):
    return render(request,'report.html')

