from django.urls import path
from .views import TargetsView

urlpatterns = [
    path('', TargetsView.as_view(), name='targets')
]
