# StudyManager/urls.py
from django.contrib import admin
from django.urls import path, include  # Include is important for adding app-specific URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('studies.urls')),  # Include URLs from the studies app
]
