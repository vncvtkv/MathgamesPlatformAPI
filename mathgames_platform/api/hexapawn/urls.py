from django.urls import path
from .views import GameListCreateView, MoveView

urlpatterns = [
    path('hexapawn/', GameListCreateView.as_view(), name='game-list'),
    path('hexapawn/<int:game_id>/move/', MoveView.as_view(), name='make-move'),
]