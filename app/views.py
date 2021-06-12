from django.shortcuts import render,redirect,reverse
from .models import *
from django.http import HttpResponse

userid=0

def index(request):
    return render(request,'index.html')


def login(request):
    global userid
    if request.method=='POST':
        uname=request.POST['username']
        password=request.POST['password']
        user_object= Clients.objects.filter(password=password,username=uname).exists()
        if user_object:
            user_obj=Clients.objects.get(password=password,username=uname)
            userid=user_obj.id
            return redirect(reverse('tasks'))
        else:
            return render(request,'register.html')
            

def tasks(request):
    global userid
    tasks = []
    flag=False
    if request.method=="POST":
        item=request.POST["title"]
        if not Task.objects.filter(title=item).exists():
            newtask=Task()
            userobj=Clients.objects.get(id=userid)
            newtask.user=userobj
            newtask.title=item
            newtask.save()
    for task in Task.objects.all():
        if task.user.id==userid:
            tasks.append(task)
    if len(tasks) != 0:
        flag=True
        return render(request,'tasks.html',context={'tasks':tasks,'id':userid,'flag':flag})
    return render(request,'tasks.html',context={'flag':flag})


def completed(request,task_id):
    for task in Task.objects.all():
        if task.id==task_id:
            task.complete=True
            task.save()
            return redirect(reverse('tasks'))
    

def remove(request,task_id):
    Task.objects.filter(id=task_id).delete()
    return redirect(reverse('tasks'))


def register(request):
    if request.method=="POST": 
        obj=Clients() 
        obj.username=request.POST['username']
        obj.password=request.POST['password'] 
        obj.email=request.POST['email'] 
        obj.save()
        return render(request,'index.html')




