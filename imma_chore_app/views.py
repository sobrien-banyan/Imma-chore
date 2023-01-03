from django.shortcuts import render
from django.views import View

# Create your views here.
class ParentView():
    def get(self. request, parent_id):

        kids = Kid.object.all()
        kid_form = KidForm()

        html_data = {
            "kid_list" : kids,
            "form" : kid_form
        }

        return render(
            request = request,
            template_name = 'parent.html',
            context = html_data,
        )


