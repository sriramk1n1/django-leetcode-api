from django.urls import path

from . import views

urlpatterns = [
    path("weekly", views.week, name="week"),
    path("leaderboard-all", views.leaderboardall, name="leaderboardall"),
    path("sync", views.sync, name="sync"),
    path("evaluate", views.evaluate, name="evaluate"),
]
