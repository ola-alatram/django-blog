
from django.urls import path
from blogsApp import views


urlpatterns = [
    path ("", views.HomeView.as_view(), name="home"),
    path ("about", views.AboutView.as_view(), name="about"),
    path ("blogs/", views.BlogsListView.as_view(), name="blogs"),
    path ("blogs/category/<slug:slug>", views.BlogsListView.as_view(), name="blogs_by_category"),
    path ("blogs/<slug:slug>", views.BlogDetailsView.as_view(), name="blog"),
    path ("api/test", views.hello_world, name="test_api"),
    path ("api/blogs", views.BlogListAPI.as_view(), name="blogsapi"),
    path ("api/blogs/<slug:slug>", views.BlogDetailsAPI.as_view(), name="blogDeAPI")
]
