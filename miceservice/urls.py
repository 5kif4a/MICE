from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index),
    path('participant', views.participant),
    path('organizer', views.Organizer.as_view()),
]

