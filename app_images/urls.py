from django.urls.conf import path
from . import views
urlpatterns = [
    path('images/', views.images, name='images'),
]