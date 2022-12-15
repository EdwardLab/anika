from django.urls import path
from django.urls import re_path
from . import views
from . import views,search
from django.urls import path
urlpatterns = [
    path('', views.anika, name='index'),
    re_path(r'^download/$', search.search_form),
    re_path(r'^anika_downloadapi', search.search),
    re_path(r'^freeapi',views.anikaapi)
]