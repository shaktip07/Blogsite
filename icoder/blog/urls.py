from django.contrib import admin
from django.urls import path, include
from .import views  

urlpatterns = [
    # API to post comment
    path('postComment', views.postComment, name="postComment"),


    path('',views.bloghome,name="bloghome"),
    path('<str:slug>',views.blogPost,name="blogPost"),
]