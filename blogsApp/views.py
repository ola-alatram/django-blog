from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from blogsApp.models import Blog, Category
from rest_framework.decorators import api_view
from rest_framework.views import APIView, Response, status
from rest_framework.response import Response
from django.db.models import Q

from blogsApp.serliazers import BlogSerializer 


# Create your views here.

class HomeView (ListView):
    template_name = "blogsApp/home.html"
    model = Category
    context_object_name = "category"

class AboutView (TemplateView):
    template_name = "blogsApp/about.html"

class BlogsListView (ListView):
    template_name = "blogsApp/blogs_list.html"
    model = Blog
    context_object_name = "BlogList"

    def get_queryset(self):
        queryset = Blog.objects.all().order_by("-date")

        category = self.kwargs.get("slug")

        if category:
            queryset = queryset.filter(category__slug=category)

        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(Q(title__contains=q) | Q(content__contains=q))

        return queryset

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context ["categories"] = Category.objects.all()
            context ["selected_category"] = self.kwargs.get("slug")    
            return context


class BlogDetailsView (DetailView):
    template_name = "blogsApp/Blog_details.html"
    model = Blog
    context_object_name = "blog"


@api_view(['Get'])
def hello_world (request):
    return Response({"message": "Hello World of Ola"})



class BlogListAPI (APIView):
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
    

class BlogDetailsAPI (APIView):
    def get(self, request, slug):
        blog = Blog.objects.get(slug = slug)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)