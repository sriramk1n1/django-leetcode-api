from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("weekly", views.week, name="week"),
    path("leaderboard-today", views.leaderboard, name="leaderboard"),
    path("leaderboard-all", views.leaderboardall, name="leaderboardall"),
    path("leaderboard-week", views.leaderboardweek, name="leaderboardweek"),
    path("sync", views.sync, name="sync"),
    path("syncweek", views.syncweek, name="syncweek"),
    path("evaluate", views.evaluate, name="evaluate"),
    path("evaluate-week", views.evaluateweek, name="evaluate-week")
]
