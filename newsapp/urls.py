from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('sports', views.sports, name="sportspage"),
    path('entertainment', views.entertainment, name="entertainmentpage"),
    path('technology', views.technology, name="technologypage"),
    path('science', views.science, name="sciencepage"),
    path('national', views.national, name="nationalpage"),
    path('world', views.world, name="worldpage"),
    path('politics', views.politics, name="politicspage"),
    path('automobile', views.automobile, name="automobilepage"),
]