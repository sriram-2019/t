from django.urls import path
from django.conf.urls import include
from third_app import views
urlpatterns = [
    path('',views.index,name="index"),
    path('',views.ct,name="ct")
    ]