from django.urls import path

from imma_chore_app.views import HomeView, ParentView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('parent/<int:parent_id>/<int:kid_id>/<int:chore_id>', ParentView.as_view(), name='parent')
]