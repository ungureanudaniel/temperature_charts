# from django import forms
# from .models import DataInput, Device
#
# choices = Device.objects.all().values_list('name', 'name')
#
# choices_list = []
#
# for item in choices:
#     choices_list.append(item)
# class AddNewRecordForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(AddNewRecordForm, self).__init__(*args, **kwargs)
#
#
#     class Meta:
#         model = DataInput
#         fields = ['devices', 'temp', 'date', 'time']
#         exclude = ['user']
#         widgets = {
#             'temp': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Introdu temperatura...'}),
#             'date': forms.DateInput(attrs={'type': 'date'}),
#             'time': forms.TimeInput(attrs={'type': 'time'}),
#             'devices': forms.Select(choices=choices_list, attrs = {'class': 'form-control'}),
#
#         }
