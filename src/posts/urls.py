from django.urls import path
from posts.views import BlogHome, BlogPostCreate , BlogPostDelete, BlogPostDelete, BlogPostDetail, BlogPostUpdate
#from django.contrib.auth.decorators import login_required

app_name = "posts"

urlpatterns = [
    path('', BlogHome.as_view(), name='home'),
    path('create/', BlogPostCreate.as_view(), name='creer'),
    #path('<str:slug>/', login_required(BlogPostDetail.as_view()), name='detail'),
    path('<str:slug>/', BlogPostDetail.as_view(), name='detail'),
    path('edit/<str:slug>/', BlogPostUpdate.as_view(), name='editer'),
    path('delete/<str:slug>/', BlogPostDelete.as_view(), name='supprimer'),
]
