from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import AddNewRecordForm

def data_input(request):
    #-------------------------------DATA INPUT VIEW-----------------------------

    if request.method=="POST":
        form = AddNewRecordForm(request.POST, request.FILES or None)
        if form.is_valid():
            try:
                newrec = form.save(commit=False)
                newrec.save()
                return redirect("/date_temperatura")
                messages.success(request, _('Succes!'))
            except Exception as e:
                print(e)
        return render(request, "users/login.html", {'form':form,})
    else:
        form = AddNewRecordForm()
    return render(request, "temperature_data/data_input.html", {'form':form,})
