from django.contrib import messages
from django.shortcuts import render, redirect

from pet_app.filters import PetRegisterFilter
from pet_app.forms import OfficerRegister,OfficerUpdateForm
from pet_app.models import Login, PetRegister,Complaint


def admin_home(request):
    return render(request, 'admintemp/admin_home.html')


def officer_register(request):
    form = OfficerRegister()
    if request.method == 'POST':
        form = OfficerRegister(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_officer = True
            user.save()
            messages.info(request, 'Officer Registered Successful')
            return redirect('officer_view')
    return render(request, 'admintemp/officer_add.html', {'form': form})


def officer_view(request):
    data = Login.objects.filter(is_officer=True)
    return render(request, 'admintemp/officer_view.html',{'data':data})


def officer_edit(request, id):
    data = Login.objects.get(id=id)
    form = OfficerUpdateForm(instance=data)
    if request.method == 'POST':
        form = OfficerUpdateForm(request.POST or None, request.FILES or None, instance=data)
        if form.is_valid():
            form.save()
            messages.info(request, 'Officer edited successful')
            return redirect('officer_view')
    return render(request, 'admintemp/officer_edit.html', {'form': form})


def officer_delete(request, id):
    data = Login.objects.get(id=id)
    if request.method == 'POST':
        data.delete()
        return redirect('officer_view')
    else:
        return redirect('officer_view')


def customer_view(request):
    data = Login.objects.filter(is_user=True)
    return render(request, 'admintemp/customer_view.html',{'data':data})

def accept_customer(request, id):
    data = Login.objects.get(id=id)
    data.status = True
    data.save()
    messages.info(request, 'User Accepted')
    return redirect('customer_view')

def reject_customer(request, id):
    data = Login.objects.get(id=id)
    data.status = False
    data.save()
    messages.info(request, 'User Rejected')
    return redirect('customer_view')


def pet_register_vi(request):
    p = PetRegister.objects.all()
    petfilter = PetRegisterFilter(request.GET, queryset=p)
    context = {
        'p': p,
        'petfilter': petfilter
    }
    return render(request, 'admintemp/pet_register_view.html', {'p': p})

def approve_pet(request,id):
    data = PetRegister.objects.get(id=id)
    data.status=1
    data.save()
    messages.info(request,'Approved')
    return redirect('pet_register_vi')

def reject_pet(request,id):
    data = PetRegister.objects.get(id=id)
    data.status=2
    data.save()
    messages.info(request,'Rejected')
    return redirect('pet_register_vi')

def pet_register_del(request, id):
    p = PetRegister.objects.get(id=id)
    if request.method == 'POST':
        p.delete()
        return redirect('pet_register_vi')
    else:
        return redirect('pet_register_vi')

def complaint_admin(request):
    n = Complaint.objects.all()
    return render(request, 'admintemp/complaint.html', {'complaint': n})

def reply_complaint(request, id):
    complaint = Complaint.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        complaint.reply = r
        complaint.save()
        messages.info(request, 'Reply send')
        return redirect('complaint_admin')
    return render(request, 'admintemp/reply_complaint.html', {'complaint': complaint})
