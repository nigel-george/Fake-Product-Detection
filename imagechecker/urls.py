from django.urls import path
from . import views

app_name = 'imagechecker'

urlpatterns = [
    
    path('upload/', views.upload_image, name='upload_image'),

    # Other URL patterns for your app
]
