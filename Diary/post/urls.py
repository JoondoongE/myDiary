from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/',views.blog, name='blog'),
    # path('itemRegist/',views.itemRegist, name='itemRegist'),
    # path('itemCreate/',views.itemCreate, name='itemCreate'),
    path('blog/<int:pk>/', views.post, name='post'),
    path('blog/write/', views.write, name='write'),
    path('blog/<int:pk>/edit/',views.edit, name='edit'),
    path('blog/<int:pk>/delete/',views.delete, name='delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)