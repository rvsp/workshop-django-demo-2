from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
# Create your views here.
from .forms import contactus

def contact_display(request):
    if request.method == 'GET':
        form = contactus()
    else:
        form = contactus(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['your_name']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                print(">>>>>>>>>>>>>> mail start to sent")
                send_mail(subject, message, [from_email], ['yourmail@domain.com'])
                print(">>>>>>>>>>>>>> mail sent")
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, "success.html")
    return render(request, "contactus.html", {'form': form})