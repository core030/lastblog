
from django.contrib import admin
from django.urls import path, include
import blog.views
from django.conf import settings
from django.conf.urls.static import static
import blogapp.views
import accounts.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"),

    path('blog/', include('blog.urls')),
    path('blogapp/', include('blogapp.urls')),
    path('accounts/',include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
