from django.urls import path

from imma_chore_app.views import HomeView, ParentView, KidView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('parent/<int:parent_id>/<int:kid_id>/<int:chore_id>', ParentView.as_view(), name='parent'),
    path('kid/<int:kid_id>/<int:chore_id>', KidView.as_view(), name='kid'),
#     path('kid/<int:kid_id>', KidChoresView.as_view(), name='kid_chore_list')
#     path('chore/<int:chore_id', ChoreView.as_view(), name='chore')
#     path('parent/<int:parent_id', ParentsKidsView.as_view(), name='parent_kid_list')
#     path('kids', KidsView.as_view(), name='kid_list')
#     path('chores', ChoresView.as_view(), name='chore_list')
#     path('parents', ParentsView.as_view(), name='parent_list')
]