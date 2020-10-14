from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('posts/', views.PostListView.as_view() , name='post_list'),
    path('posts/create/', views.PostCreateView.as_view() , name='post_create'),
    path('posts/<slug>', views.PostDetailView.as_view() , name='post_details'),

]