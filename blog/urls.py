
from django.contrib import admin
from django.urls import path
import blog.views
from django.conf import settings
from django.conf.urls.static import static
import blogapp.views
urlpatterns = [
    path('blog/<int:blog_id>', blog.views.detail, name="detail"),
    path('blog/new/', blog.views.new, name='new'),
    path('blog/create/', blog.views.create, name='create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# blog에 필요한 url만 남기기