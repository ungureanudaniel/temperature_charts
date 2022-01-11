from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from .forms import CaptchaForm
#-------------------------------LOGIN VIEW-----------------------------------
# @csrf_protect
def user_login(request):
    template = 'users/login.html'
    # form = CaptchaForm(request.POST)

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            try:
                login(request, user)

                return redirect("account")
                messages.success(request, "Succes!")
            except Exception as e:
                print(e)

        else:
            messages.error(request, "Date de logare incorecte!")
            return render(request, template, {})
            # return redirect("login")
    else:
        return render(request, template, {})

#-------------------------------REGSTER VIEW-----------------------------------
def register(request):
    if request.method=="POST":
        username = request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        phone = request.POST['phone']
        gender = request.POST['gender']
        image = request.FILES['image']

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('/register')

        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password1)
        applicants = Applicant.objects.create(user=user, phone=phone, gender=gender, image=image, type="applicant")
        user.save()
        applicants.save()
        return render(request, "users/login.html")
    return render(request, 'users/register.html')

@login_required
def account(request):
    context = {
        'account_page': "active",
    }
    return render(request, 'users/account.html', context)

def privacy(request):
    return render(request, 'users/privacy.html')


def terms(request):
    return render(request, 'users/terms.html')


def contact(request):
    template_name = 'users/contact.html'
    #--------------logo------------------------------
    # logos = Logo.objects.filter(status='active')
    form = CaptchaForm(request.POST)
    if request.method == "POST":
        message_name = request.POST.get('message-name')
        message_email = request.POST.get('message-email')
        message = request.POST.get('message')
        #send email
        if message and message_name and message_email:
            if form.is_valid():
                try:
                    send_mail(
                    message_name,
                    message,
                    message_email,
                    ['danielungureanu531@gmail.com']
                    )
                    messages.success(request, "Thank you for writting me {}! I will answer ASAP.".format(message_name))
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return HttpResponseRedirect('/contact/')
            else:

                messages.warning(request, "Failed! Please fill in the captcha field again!")
                return HttpResponseRedirect('/contact/')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')

        render(request, template_name, {'message_name': message_name, 'categories': categories, 'form': form,})
    else:
        return render(request, template_name, {'form': form})

#--------------------------ABOUT VIEW -----------------------------------------
def about(request):
    template_name = 'users/about.html'
    
    context = {
    }
    return render(request, template_name, context)
