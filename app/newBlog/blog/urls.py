from django.urls import path
from django.conf.urls import url

from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:id>/', views.single, name='single'),
    path('post/new/', views.postCreate, name='post_create'),
###    path('post/<int:id>/edit/', views.PostEdit, name='post_edit'),
    url('user/login/', views.LoginFormView.as_view(), name='login'),
    path('user/register/', views.RegisterFormView.as_view(), name="register"),
    path('post/<int:id>/comment/', views.AddComment, name='add_comment'),
]
