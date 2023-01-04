from django.urls import path
from . import views


urlpatterns = [
    path('', views.artice_list, name='list'),
    # path(r'^(?P<slug>[\w]+)/$', views.artice_detail),
    path('<slug>/', views.artice_detail, name='detail'),
]
