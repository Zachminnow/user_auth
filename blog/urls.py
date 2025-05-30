from django.urls import path
from .views import PostDetailView, PostListView
from django.contrib.auth import views as auth_views
from .views import RegisterView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        next_page="login"), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
