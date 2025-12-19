from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import Contact


# Home page
def home(request):
    return render(request, 'home.html')


# About page
def about(request):
    return render(request, 'about.html')


# Contact page
def contact(request):
    if request.method == 'POST':
        Contact.objects.create(
            name=request.POST.get('name'),
            mobile=request.POST.get('mobile'),
            email=request.POST.get('email'),
            message=request.POST.get('message')
        )
        # redirect with success flag
        return redirect('/contact/?success=1')

    success = request.GET.get('success')
    return render(request, 'contact.html', {'success': success})


# Messages list (admin only)
@login_required
def messages_list(request):
    messages = Contact.objects.all().order_by('-id')
    return render(request, 'messages.html', {'messages': messages})


# Delete message
@login_required
def delete_message(request, id):
    msg = get_object_or_404(Contact, id=id)
    msg.delete()
    return redirect('messages')


# Reply to message + send email
@login_required
def reply_message(request, id):
    msg = get_object_or_404(Contact, id=id)

    if request.method == 'POST':
        reply_text = request.POST.get('reply')

        msg.reply = reply_text
        msg.replied = True
        msg.save()

        send_mail(
            subject='Reply to your message',
            message=reply_text,
            from_email=None,
            recipient_list=[msg.email],
            fail_silently=False,
        )

        return redirect('messages')

    return render(request, 'reply.html', {'msg': msg})
