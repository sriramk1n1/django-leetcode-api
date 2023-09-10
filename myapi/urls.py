from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("weekly", views.week, name="week"),
    path("leaderboard-today", views.leaderboard, name="leaderboard"),
    path("leaderboard-all", views.leaderboardall, name="leaderboard"),
    path("sync", views.sync, name="sync"),
    path("evaluate", views.evaluate, name="evaluate")
]
