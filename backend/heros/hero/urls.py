from django.urls import path
from .views import GenrateHero, Fight, Champion

urlpatterns = [
    path('hero/', GenrateHero.as_view(), name='GenrateHero'),
    path('fight/', Fight.as_view(), name='Fight'),
    path('champion/', Champion.as_view(), name='Champion'),
]
