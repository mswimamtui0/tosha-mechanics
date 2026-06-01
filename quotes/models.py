from django.db import models
from django.contrib.auth.models import User

class Quote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_title = models.CharField(max_length=200)
    service_type = models.CharField(max_length=50, choices=[
        ('engineering', 'Mechanical Engineering'),
        ('welding', 'Welding'),
        ('fabrication', 'Fabrication'),
        ('other', 'Other'),
    ])
    location = models.CharField(max_length=200, help_text="Where is the problem/site located?")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending', choices=[
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ])
    
    def __str__(self):
        return f"{self.user.username} - {self.project_title}"

class Message(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE, related_name='messages', null=True, blank=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages', null=True, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.sender.username} -> {self.subject[:50]}"
    
    class Meta:
        ordering = ['-created_at']

class ContactInquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    is_replied = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.subject[:50]}"