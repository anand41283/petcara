from django.contrib import messages
from django.shortcuts import render, redirect
from pet_app.forms import PetRegisterForm,SchdeuleForm
from pet_app.models import PetRegister,Login,Schedule,Appointment


def officer_home(request):
    return render(request, 'officertemp/officer_home.html')

def pet_register_officer(request):
    form = PetRegisterForm()
    if request.method == 'POST':
        form = PetRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pet_register_vie')
    return render(request,'officertemp/pet_register.html',{'form':form})

def pet_register_vie(request):
    p = PetRegister.objects.all()
    return render(request, 'officertemp/pet_register_view.html', {'p': p})


def pet_update(request, id):
    s = PetRegister.objects.get(id=id)
    if request.method == 'POST':
        form = PetRegisterForm(request.POST or None, instance=s)
        if form.is_valid():
            form.save()
            messages.info(request, 'schdeule updated')
            return redirect('pet_register_vie')
    else:
        form = PetRegisterForm(instance=s)
    return render(request, 'officertemp/pet_register_edit.html', {'form': form})

def pet_delete(request,id):
    data = PetRegister.objects.get(id=id)
    data.delete()
    return redirect('pet_register_vie')

def schedule_add(request):
    form = SchdeuleForm()
    if request.method == 'POST':
        form = SchdeuleForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.customer = Login.objects.get(username=request.user)
            form.save()
            messages.info(request, 'schedule added successful')
            return redirect('schedule_view')
    return render(request,'officertemp/schdeule_add.html',{'form':form})

def schedule_view(request):
    cus = Login.objects.get(username=request.user)
    s = Schedule.objects.filter(customer=cus)
    context = {
        'schedule': s
    }
    return render(request,'officertemp/schedule_view.html',context)

def schedule_update(request, id):
    s = Schedule.objects.get(id=id)
    if request.method == 'POST':
        form = SchdeuleForm(request.POST or None, instance=s)
        if form.is_valid():
            form.save()
            messages.info(request, 'schdeule updated')
            return redirect('schedule_view')
    else:
        form = SchdeuleForm(instance=s)
    return render(request, 'officertemp/schedule_update.html', {'form': form})

def schedule_delete(request, id):
    s = Schedule.objects.filter(id=id)
    if request.method == 'POST':
        s.delete()
        return redirect('schedule_view')

def appointment_view_doctor(request):
    data1 = Schedule.objects.get(customer=request.user)
    print(data1)
    data = Appointment.objects.filter(schedule=data1)
    print(data)
    return render(request, 'officertemp/appointment_view.html', {'data': data})

def approve_appointment(request, id):
    n = Appointment.objects.get(id=id)
    n.status = 1
    n.save()
    messages.info(request, 'Appointment  Confirmed')
    return redirect('appointment_view_doctor')

def reject_appointment(request, id):
    n = Appointment.objects.get(id=id)
    n.status = 2
    n.save()
    messages.info(request, 'Appointment Rejected')
    return redirect('appointment_view_doctor')


