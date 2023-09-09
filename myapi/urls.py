from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("weekly", views.week, name="week"),
    path("progress", views.progress, name="progress"),
    path("leaderboard-today", views.leaderboard, name="leaderboard"),
    path("leaderboard-all", views.leaderboardall, name="leaderboard"),
    path("sync", views.sync, name="leaderboard"),
    path("evaluate", views.sync, name="leaderboard")
]