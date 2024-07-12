from django.urls import path
from .views import schedule_view

urlpatterns = [
    path('', schedule_view, name='schedule'),
]
