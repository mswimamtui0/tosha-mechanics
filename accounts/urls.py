from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('inbox/', views.inbox_view, name='inbox'),
    path('send-message/', views.send_message_view, name='send_message'),
    path('send-reply/<int:message_id>/', views.send_reply_view, name='send_reply'),
]