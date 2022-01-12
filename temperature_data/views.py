from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
# from .forms import AddNewRecordForm
# from .models import DataInput
#
# def data_input(request):
#     # -------------------------------DATA INPUT VIEW----------------------------
#     form = AddNewRecordForm(request.POST, request.FILES or None)
#     if request.method=="POST":
#
#         if form.is_valid():
#             try:
#                 data = form.cleaned_data
#                 data_inpt = DataInput.objects.create(**data, user=request.user)
#                 # form.save()
#                 messages.success(request, _('Succes!'))
#                 return redirect("/date_temperatura")
#
#             except Exception as e:
#                 print(e)
#     else:
#         form = AddNewRecordForm()
#     return render(request, "temperature_data/data_input.html", {'form':form,})
