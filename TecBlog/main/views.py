from django.shortcuts import render

# Create your views here.
def TecBlogpage(request):
    return  render(request, template_name = 'main/TecBlog.html')