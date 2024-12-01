from django.urls import path
from . import views

app_name = "post"

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('post/<int:pk>/', views.show_post, name='post'),
    path('add_post/', views.AddPost.as_view(), name='add_post'),
    path('update_post/<int:pk>', views.UpdatePost.as_view(), name='update_post'),
    path('post/<int:pk>/delete', views.DeletePost.as_view(), name='delete_post'),
]
