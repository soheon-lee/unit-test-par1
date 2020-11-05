from django.urls import path

from .views import JustView

urlpatterns = [
    path('', JustView.as_view()),
]
