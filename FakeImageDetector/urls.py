from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_imagechecker(request):
    return redirect('imagechecker:upload_image')  # Use the namespace here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('imagechecker/', include('imagechecker.urls', namespace='imagechecker')),  # Use the namespace here
    path('', redirect_to_imagechecker),
]
