from django.urls import path
from . import views

urlpatterns = [
    path('request/', views.request_quote, name='request_quote'),
    path('my-quotes/', views.my_quotes, name='my_quotes'),
]