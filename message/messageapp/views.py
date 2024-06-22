from django.shortcuts import render,HttpResponse,redirect
from messageapp.models import Msg
# Create your views here.
def create(request):
    print("request is:",request.method)
    if request.method=='GET':
        #print("in if section")
        return render(request,'create.html')
    else:
        #fetch data from form
        n=request.POST['uname']
        e=request.POST['uemail']
        m=request.POST['mobile']
        msg=request.POST['msg']
        # print(n)
        # print(e)
        # print(m)
        # print(msg)
        #insert
        m=Msg.objects.create(name=n,email=e,mobile=m,msg=msg)
        m.save()
        #return HttpResponse("data inserted successfully")
        return redirect('/dash')
def dashboard(request):
    m=Msg.objects.all()
    print(m)
    print(m[0])
    print(m[0].name)
    print(m[1].email)
    context={}
    context['data']=m
    #return HttpResponse("data fetch from database")
    return render(request,'dashboard.html',context)
def delete(request,rid):
    m=Msg.objects.filter(id=rid)
    m.delete()
    return redirect('/dash')
def edit(request,rid):
    d=Msg.objects.get(id=rid)
    print(d)
    if request.method=='POST':
        n=request.POST['uname']
        e=request.POST['uemail']
        m=request.POST['mobile']
        msg=request.POST['msg']
        k=Msg.objects.filter(id=rid).update(name=n,email=e,mobile=m,msg=msg)
        return redirect('/dash')
    context={}
    context['data']=d
    return render(request,'edit.html',context)