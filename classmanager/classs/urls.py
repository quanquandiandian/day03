from django.urls import path
from classs.views import index

urlpatterns = [
    path('index/',index)
]