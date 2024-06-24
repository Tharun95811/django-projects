from django.urls import path
from studentcourse.views import home
urlpatterns = [path('', home),]