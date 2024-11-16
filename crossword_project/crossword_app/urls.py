from django.urls import path
from . import views

urlpatterns = [
    path('', views.crossword_view, name='crossword'),
    path('validate/', views.validate_answer, name='validate_answer'),
    path('success/', views.success_view, name='success'),
]
