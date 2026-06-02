from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.contrib import messages
import json
from .models import Post, Service, CaseStudy
from quotes.models import ContactInquiry

def home(request):
    services = Service.objects.all()
    posts = Post.objects.all().order_by('-created_at')[:3]
    featured_cases = CaseStudy.objects.filter(is_featured=True)[:3]
    return render(request, 'core/home.html', {
        'services': services,
        'posts': posts,
        'featured_cases': featured_cases,
    })

def work_view(request):
    posts = Post.objects.all().order_by('-created_at')
    # Convert posts to JSON for JavaScript filtering
    posts_json = []
    for post in posts:
        posts_json.append({
            'id': post.id,
            'title': post.title,
            'description': post.description,
            'category': post.category,
            'created_at': post.created_at.strftime('%Y-%m-%d'),
        })
    return render(request, 'core/work.html', {
        'posts': posts,
        'posts_json': json.dumps(posts_json),
    })

def about_view(request):
    return render(request, 'core/about.html')

def case_studies_view(request):
    cases = CaseStudy.objects.all()
    return render(request, 'core/case_studies.html', {'cases': cases})

def case_detail_modal(request, id):
    case = get_object_or_404(CaseStudy, id=id)
    return render(request, 'core/case_detail_modal.html', {'case': case})

def project_detail_modal(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'core/project_detail_modal.html', {'post': post})

def contact_view(request):
    success = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message_text = request.POST.get('message')
        
        inquiry = ContactInquiry.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message_text
        )
        success = True
        
    return render(request, 'core/contact.html', {'success': success})