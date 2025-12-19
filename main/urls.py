from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('messages/', views.messages_list, name='messages'),
    path('delete/<int:id>/', views.delete_message, name='delete_message'),
path('reply/<int:id>/', views.reply_message, name='reply_message'),

]
