from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django import forms
from django.contrib.auth.models import User
from quotes.models import Message
from .models import Profile

class SignUpForm(UserCreationForm):
    phone = forms.CharField(max_length=20, required=True, help_text='Contact phone number')
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super().save(commit=True)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            profile = user.profile
            profile.phone = self.cleaned_data['phone']
            profile.save()
        return user

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def dashboard_view(request):
    unread_count = Message.objects.filter(receiver=request.user, is_read=False).count()
    return render(request, 'accounts/dashboard.html', {'unread_count': unread_count})

@login_required
def inbox_view(request):
    user_messages = Message.objects.filter(sender=request.user) | Message.objects.filter(receiver=request.user)
    user_messages = user_messages.distinct().order_by('-created_at')
    return render(request, 'accounts/inbox.html', {'messages': user_messages})

@login_required
def send_message_view(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message_text = request.POST.get('message')
        
        # Get admin user (assuming admin user with id=1 or is_superuser)
        admin_user = User.objects.filter(is_superuser=True).first()
        
        if admin_user:
            Message.objects.create(
                sender=request.user,
                receiver=admin_user,
                subject=subject,
                message=message_text
            )
            messages.success(request, 'Message sent successfully!')
        else:
            messages.error(request, 'Unable to send message. Please try again later.')
        
        return redirect('inbox')
    
    return render(request, 'accounts/send_message.html')

@login_required
def send_reply_view(request, message_id):
    original_message = get_object_or_404(Message, id=message_id)
    
    if request.method == 'POST':
        reply_text = request.POST.get('reply_message')
        if reply_text:
            Message.objects.create(
                sender=request.user,
                receiver=original_message.sender,
                subject=f"Re: {original_message.subject}",
                message=reply_text
            )
            messages.success(request, 'Reply sent successfully!')
    
    return redirect('inbox')