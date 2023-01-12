from django.urls import path

from imma_chore_app.views import HomeView, ParentView, KidView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('parent/<int:parent_id>/<int:kid_id>/<int:chore_id>', ParentView.as_view(), name='parent'),
    path('kid/<int:kid_id>/<int:chore_id>', KidView.as_view(), name='kid'),
    
]