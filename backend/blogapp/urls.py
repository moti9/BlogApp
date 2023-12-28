from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path('blogs/<uuid:pk>/', views.BlogDetailView.as_view(), name='blog-detail'),
    path("blogs/", views.BlogListView.as_view(), name="get_blogs"),
    path("newblog/", views.BlogCreateView.as_view(), name="new_blog"),
    path("tags/", views.TagListView.as_view(), name="get_tags"),
    path("update/<uuid:pk>", views.BlogUpdateView.as_view(), name="update_blog"),
]