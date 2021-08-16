from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
]

if not settings.DEBUG:
    handler404 = "base.views.page_not_found"
