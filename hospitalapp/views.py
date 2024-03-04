from django.shortcuts import render, redirect
from hospitalapp.models import Member, Patient, Users, Products


# Create your views here.
def index(request):
    if request.method == 'POST':
        patient = Patient(fullname=request.POST['name'],
                          email=request.POST['email'],
                          phone=request.POST['phone'],
                          date=request.POST['date'],
                          department=request.POST['department'],
                          doctor=request.POST['doctor'],
                          message=request.POST['message'])
        patient.save()
        return redirect('/')
    else:
        return render(request, 'index.html')


def inner(request):
    return render(request, 'inner-page.html')


def register(request):
    if request.method == 'POST':
        member = Member(username=request.POST['username'], email=request.POST['email'],
                        password=request.POST['password'])
        member.save()
        return redirect('/login')
    else:
        return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def upload(request):
    return render(request, 'upload.html')


def form(request):
    return render(request, 'form.html')


def appointmentdetails(request):
    myappoint = Patient.objects.all()
    return render(request, 'Appointmentdetails.html', {'myappoint': myappoint})


def users(request):
    myusers = Users.objects.all()
    return render(request, 'user.html', {'myusers': myusers})


def details(request):
    myproducts = Products.objects.all()
    return render(request, 'details.html', {'myproducts': myproducts}),


def adminhome(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'],
                                 password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'],
                                        password=request.POST['password'])
            return render(request, 'adminhome.html', {'member': member})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
