from django.conf.urls import path
from .views import index
urlpatterns = [
   path ('', index, name='index'),
]