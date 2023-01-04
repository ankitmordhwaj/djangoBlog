from django.urls import path
from . import views


urlpatterns = [
    path('', views.artice_list),
    # path('', views.home),
]
