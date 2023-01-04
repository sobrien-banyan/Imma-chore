from django.shortcuts import render
from django.views import View

from django.views import View

# Create your views here.

class HomeView(View):
    def get(self, request):

        return render(
            request=request,
            template_name='index.html',
            context={}
        )
class ParentView():
    def get(self. request, parent_id):
        parent = Parent.object.all()
        # kids = Kid.object.all()
        # kid_form = KidForm()
        html_data{
            "parent" : parent
        }
        
        # html_data = {
        #     "kid_list" : kids,
        #     "form" : kid_form
        # }

        return render(
            request = request,
            template_name = 'parent.html',
            context = html_data,
        )


