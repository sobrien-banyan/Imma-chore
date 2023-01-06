from django.shortcuts import render
from django.views import View

from django.views import View
from imma_chore_app.forms import ParentForm, KidForm, ChoreForm
from imma_chore_app.models import Parent, Kid, Chore

# Create your views here.

class HomeView(View):
    def get(self, request):

        return render(
            request=request,
            template_name='index.html',
            context={}
        )


class ParentView(View):
    def get(self, request, parent_id=1):
        # parent = Parent.objects.all()
        # kids = Kid.object.all()
        # kid_form = KidForm()
        parent = Parent.objects.get(parent_id)
        kids = Kid.objects.all()
        kid_form = KidForm()
        chore_form = ChoreForm()
        html_data = {
            'kid_list' : kids,
            'kid_form' : kid_form,
            'chore_form' : chore_form,
            'parent_id' : parent[0].id
        }

        # html_data = {
        #     "parent" : parent
        # }
        
        # html_data = {
        #     "kid_list" : kids,
        #     "form" : kid_form
        # }

        return render(
            request = request,
            template_name = 'parent.html',
            context = html_data,
        )

    def post(self, request, parent_id=1):
        parent = parent_id
        kid_form = KidForm(request.POST)
        kid_form.save()

        return redirect('parent')

