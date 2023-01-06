from django.urls import path

from imma_chore_app.views import HomeView, ParentView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('parent', ParentView.as_view(), name='parent')
]