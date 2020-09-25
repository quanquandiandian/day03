from django.urls import path

from book1.views import player,register,json

urlpatterns=[
    path('<team_id>/<player_id>',player),
    path('register/',register),
    path('json/',json)
]