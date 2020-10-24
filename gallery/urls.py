from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.galleryView, name="gallery"),
    path('upload/', views.addImage, name="upload"),
    path('view/<int:id>', views.viewImage, name='view-image'),
    path('view/delete/<int:id>', views.removeImage, name='remove-image'),
    path('delete/all', views.removeAllImages, name='remove-all-images'),
]