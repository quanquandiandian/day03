from django.urls import path

from book1.views import player

urlpatterns=[
    path('<team_id>/<player_id>',player)
]