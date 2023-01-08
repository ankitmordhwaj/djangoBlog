from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.artice_list, name='list'),
    # path(r'^(?P<slug>[\w]+)/$', views.artice_detail),
    path('create', views.artice_create, name='create'),
    path('<slug>/', views.artice_detail, name='detail'),
]
