from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('work/', views.work_view, name='work'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('case-studies/', views.case_studies_view, name='case_studies'),
    path('case-study/<int:id>/', views.case_detail_modal, name='case_detail_modal'),
    path('project-detail/<int:id>/', views.project_detail_modal, name='project_detail_modal'),
]