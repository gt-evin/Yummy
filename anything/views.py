from django.shortcuts import render, redirect

from anything.forms import ImageUploadForm
from anything.models import Member, ImageModel
from anything.models import Booking, Users, Products


# Create your views here.
def index(request):
    if request.method == 'POST':
        name = Booking(name=request.POST['name'],
                       email=request.POST['email'],
                       phone=request.POST['phone'],
                       date=request.POST['date'],
                       time=request.POST['time'],
                       people=request.POST['people'],
                       message=request.POST['message'])
        name.save()
        return redirect('/')
    else:
        return render(request, 'index.html')


def inner(request):
    return render(request, 'sample-inner-page.html')


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


def appointmentdetails(request):
    myappoint = Booking.objects.all
    return render(request, 'appointmentdetails.html', {'myappoint': myappoint})


def users(request):
    myusers = Users.objects.all
    return render(request, 'user.html', {'myusers': myusers})


def details(request):
    myproducts = Products.objects.all()
    return render(request, 'details.html', {'myproducts': myproducts})


def adminhome(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'], password=request.POST['password'])
            return render(request, 'adminhome.html', {'member': Member})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})


def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'showimages.html', {'images': images})


def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/showimage')
