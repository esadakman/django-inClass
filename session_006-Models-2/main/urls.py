from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from fscohort.views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('fscohort/', include('fscohort.urls')),  # -> fscohort/urls.py
]

# View Static/Media Files:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
