from django.contrib import messages
from django.shortcuts import render, redirect

from pet_app.forms import PetRegisterForm,ComplaintForm
from pet_app.models import PetRegister,Login,Schedule,Appointment,Complaint


def user_home(request):
    return render(request, 'usertemp/user_home.html')


def officer_view(request):
    data = Login.objects.filter(is_officer=True)
    return render(request, 'usertemp/officer_view.html',{'data':data})


def pet_register(request):
    form = PetRegisterForm()
    if request.method == 'POST':
        form = PetRegisterForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.customer=Login.objects.get(username=request.user)
            form.save()
            messages.info(request, 'pet Registeration Complete')
            return redirect('pet_register_view')
    return render(request, 'usertemp/pet_register.html', {'form': form})


def pet_register_view(request):

    p = PetRegister.objects.filter(owner=request.user.name)
    return render(request, 'usertemp/pet_register_view.html', {'p': p})

def view_schedule_customer(request):
    s = Schedule.objects.all()
    context = {
        'schedule': s
    }
    return render(request, 'usertemp/schedule_view.html', context)

def take_appointment(request, id):
    s = Schedule.objects.get(id=id)
    c = Login.objects.get(username=request.user)
    appointment = Appointment.objects.filter(userperson=c, schedule=s)
    if appointment.exists():
        messages.info(request, 'You Have Already Requested Appointment for this Schedule')
        return redirect('view_schedule_customer')
    else:
        if request.method == 'POST':
            obj = Appointment()
            obj.userperson = c
            obj.schedule = s
            obj.save()
            messages.info(request, 'Appointment Booked Successfully')
            return redirect('appointment_view')
    return render(request, 'usertemp/take_appointment.html', {'schedule': s})

def appointment_view(request):
    c = Login.objects.get(username=request.user)
    a = Appointment.objects.filter(userperson=c)
    return render(request, 'usertemp/appointment_view.html', {'appointment': a})

def complaint_add_user(request):
    form = ComplaintForm()
    u = request.user
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.userperson = u
            obj.save()
            messages.info(request, 'Discussion Registered')
            return redirect('complaint_user')
    else:
        form = ComplaintForm()
    return render(request, 'usertemp/complaint_add.html', {'form': form})

def complaint_user(request):
    n = Complaint.objects.filter(userperson=request.user)
    return render(request, 'usertemp/complaint.html', {'complaint': n})