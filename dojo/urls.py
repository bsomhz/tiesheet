from django.urls import path
from dojo.views import DojoListView

urlpatterns = [
    path('', DojoListView.as_view()),
]
