from django.conf import settings

from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    path('db', views.db),
    path('search',views.search),

]