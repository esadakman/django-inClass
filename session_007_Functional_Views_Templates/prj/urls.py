
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("fs", include('fsApp.urls')),
    path("ds", include('dsApp.urls'))
]
