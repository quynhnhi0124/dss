from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('filter', views.gv_filter, name='filter'),
    # path()
]