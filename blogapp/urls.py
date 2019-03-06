
from django.contrib import admin
from django.urls import path
import blog.views
from django.conf import settings
from django.conf.urls.static import static
import blogapp.views
urlpatterns = [
    path('blogapp/',blogapp.views.twohome, name="twohome"),
    path('blogapp/<int:twoblog_id>', blogapp.views.twodetail, name="twodetail"),
    path('blogapp/twonew/', blogapp.views.twonew, name='twonew'),
    path('blogapp/twocreate/', blogapp.views.twocreate, name='twocreate'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# blogapp에 필요한 url만 남기기