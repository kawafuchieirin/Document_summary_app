# crossword_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.crossword_view, name='crossword_puzzle'),
    path('validate_answer/', views.validate_answer, name='validate_answer'),
    path('success/', views.success_view, name='success'),
]
