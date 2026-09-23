from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, ListView, DetailView
from blogsApp.forms import ContactForm
from blogsApp.models import Blog, Category, ContactMessage
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
    paginate_by = 2

    def get_queryset(self):
        queryset = Blog.objects.all().order_by("-date")

        category = self.kwargs.get("slug")

        if category:
            queryset = queryset.filter(category__slug=category)

        search_text = self.request.GET.get('search_text')
        if search_text:
            queryset = queryset.filter(Q(title__contains=search_text) | Q(content__contains=search_text))

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        current_blog = self.object 

        related_blogs = Blog.objects.filter(
            category__in = current_blog.category.all()
            ).distinct().exclude(id = current_blog.id
                      ).order_by("-date")[:3]
        
        context ["related_blogs"] = related_blogs

        return context

class ContactView (FormView):
    form_class = ContactForm 
    template_name = "blogsApp/contact_me.html"
    success_url = reverse_lazy("contact_success")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ContactSuccessView(TemplateView):
    template_name = "blogsApp/contact_success.html"

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