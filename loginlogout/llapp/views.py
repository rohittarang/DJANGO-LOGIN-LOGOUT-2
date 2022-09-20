from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm
from django.core.files.storage import FileSystemStorage
from .models import Master

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)

def InsertDataentry(request):
    if request.method == "POST":
        tid = request.POST['ticketid']
        sdetails = request.POST['serverdetails']
        sdate = request.POST['senddate']
        lno = request.POST['licenseno']

        vfile = request.FILES['uploadfile']
        fs = FileSystemStorage()
        filename = fs.save(vfile,vfile)
        uploadedviewfile = fs.url(filename)
    
        t_id = Master.objects.get(id=tid)
        # newdataentry = UserLogin.objects.create(ticket_id=t_id,userserverdetails=sdetails, usersenddate=sdate, userlicenseno=lno, userfile=vfile)
        # newdataentry.save()
                        
        return redirect('showuserdata')