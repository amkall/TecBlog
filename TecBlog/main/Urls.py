from django.urls import path
from main import views
urlpatterns = [
    path('TecBlog/', views.TecBlogpage, name = 'TecBlog'),
]