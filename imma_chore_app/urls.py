from django.urls import path

from imma_chore_app.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]