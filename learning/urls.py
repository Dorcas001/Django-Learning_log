
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='learn-home'),
    path('about', views.about, name ='learn-about'),
    path('topic/', views.topic, name = "topic"),
    path('topics/<int:topic_id>/', views.topic_details, name="detail"),
    path('new_entry/<int:topic_id>/', views.new_entry, name="learn-new-entry"),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name="learn-edit_entry"),
    path('new_topic/', views.new_topic, name = "learn-new-topic"),
]
