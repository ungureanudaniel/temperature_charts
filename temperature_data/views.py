from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import AddNewRecordForm
from .models import DataInput

def data_input(request):
    # -------------------------------DATA INPUT VIEW----------------------------

    if request.method=="POST":
        form = AddNewRecordForm(request.POST, request.FILES or None)
        if form.is_valid():
            try:
                temper = form.cleaned_data['temp']
                device = form.cleaned_data['devices']
                date1 = form.cleaned_data['date']
                time1 = form.cleaned_data['time']

                data_inpt = DataInput(user=request.user, temp=temper, devices = device, date = date1, time = time1)
                data_inpt.save()
                messages.success(request, _('Succes!'))
                return redirect("/date_temperatura")

            except Exception as e:
                print(e)
    else:
        form = AddNewRecordForm()
    return render(request, "temperature_data/data_input.html", {'form':form,})
