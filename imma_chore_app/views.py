from django.shortcuts import render, redirect
from django.views import View

from django.views import View
from imma_chore_app.forms import ParentForm, KidForm, ChoreForm, Kid_ChoreForm
from imma_chore_app.models import Parent, Kid, Chore, Kid_Chore

# Create your views here.

class HomeView(View):
    def get(self, request):

        parents = Parent.objects.all()
        kids = Kid.objects.all()
        html_data = {
            'parent_form' : ParentForm(),
            'parents': parents,
            'kids': kids
        }

        return render(
            request=request,
            template_name='index.html',
            context= html_data,
        )

    def post(self, request):

        if 'create' in request.POST:
            parent_form = ParentForm(request.POST)
            parent = parent_form.save()

            return redirect(f'parent/{parent.id}/1/1')

        elif 'selected_parent' in request.POST:
            parent_id = request.POST['selected_parent']
            kids = Kid.objects.all().filter(parent_id=parent_id)
            chores = Chore.objects.all().filter(parent_id=parent_id)
            kid_id = 0
            chore_id = 0
            if len(kids) > 0:
                kid_id = kids[0].id

            if len(chores) > 0:
                chore_id = chores[0].id

            return redirect(f'parent/{parent_id}/{kid_id}/{chore_id}')

        elif 'selected_kid' in request.POST:
            kid_id = request.POST['selected_kid']

            return redirect(f'kid/{kid_id}')

class ParentView(View):

    parent_object = {}

    def get(self, request, parent_id, kid_id, chore_id):
        parent = Parent.objects.get(id=parent_id)
        kids = Kid.objects.all().filter(parent_id=parent_id)
        chores = Chore.objects.all().filter(parent_id = parent_id)
        selected_kid_chores = Kid_Chore.objects.all().filter(kid_id=kid_id).filter(parent_id=parent_id).select_related('chore')
        kid_chores = Kid_Chore.objects.all().filter(parent_id = parent_id).filter(chore_id= chore_id)
        kid_form = KidForm()
        chore_form = ChoreForm()
        kid_chore_form = Kid_ChoreForm()

        chore_ready_for_deletion = False
        if len(kid_chores) == 0:
            chore_ready_for_deletion = True

        html_data = {
            'kid_list' : kids,
            'kid_form' : kid_form,
            'chore_form' : chore_form,
            'kid_chore_form': kid_chore_form,
            'parent' : parent,
            'selected_kid' : kid_id,
            'chores' : chores,
            'selected_chore_id': chore_id,
            'selected_kid_chores': selected_kid_chores,
            'chore_ready_for_deletion': chore_ready_for_deletion,
        }

        return render(
            request = request,
            template_name = 'parent.html',
            context = html_data,
        )

    def post(self, request, parent_id, kid_id, chore_id):
        if 'add_child' in request.POST:
            saved_kid = KidForm(request.POST).save()
            saved_kid.parent_id = parent_id
            saved_kid.allowance_earned = 0.0
            saved_kid.save()

            return redirect(f'/parent/{parent_id}/{saved_kid.id}/{chore_id}')

        elif 'create_chore' in request.POST:
            chore = ChoreForm(request.POST).save()
            chore.parent_id = parent_id
            chore.save()

            return redirect(f'/parent/{parent_id}/{kid_id}/{chore.id}')

        elif 'assign_chore' in request.POST:
            if kid_id == 0 or chore_id == 0:
                return redirect(f'/parent/{parent_id}/{kid_id}/{chore_id}')
            else:
                saved_kid_chore = Kid_ChoreForm(request.POST).save()
                saved_kid_chore.day_of_the_week = request.POST['day_of_the_week']
                saved_kid_chore.kid_id = kid_id
                saved_kid_chore.parent_id = parent_id
                saved_kid_chore.chore_id = chore_id
                saved_kid_chore.save()
                return redirect(f'/parent/{parent_id}/{kid_id}/{chore_id}')

        elif 'delete_kid_chore' in request.POST:
            kid_chore_id = request.POST['chore_number']
            Kid_Chore.objects.get(id = kid_chore_id).delete()

            return redirect(f'/parent/{parent_id}/{kid_id}/{chore_id}')

        elif 'delete_chore' in request.POST:
            chore_id = request.POST['chore_id']
            Chore.objects.get(id=chore_id).delete()

            return redirect(f'/parent/{parent_id}/{kid_id}/{chore_id}')

        elif 'delete_parent' in request.POST:
            parent_id = request.POST['parent_id']
            Parent.objects.get(id=parent_id).delete()

            return redirect(f'/')

        elif 'delete_kid' in request.POST:
            selected_kid_id = request.POST['kid_id']
            Kid.objects.get(id = selected_kid_id).delete()
            kids = Kid.objects.all().filter(parent_id=parent_id)
            kid_id_path_param = 0
            if len(kids) > 0:
                kid_id_path_param = kids[0].id
                
            return redirect(f'/parent/{parent_id}/{kid_id_path_param}/{chore_id}')
        else: 
            return redirect(f'/parent/{parent_id}/{kid_id}/{chore_id}')
        
class KidView(View):


    def get(self, request, kid_id):
        kid_chore_complete_form = Kid_ChoreForm()
        selected_kid_chores = Kid_Chore.objects.all().filter(kid_id=kid_id).select_related('chore')
        kid_name = Kid.objects.get(id = kid_id).name
        first_chore_id = 1
        allowance_earned = Kid.objects.get(id = kid_id).allowance_earned
        if len(selected_kid_chores) > 1:
            first_chore_id = selected_kid_chores[0].id

        html_data = {
            'kid_id' : kid_id,
            'kid_name' : kid_name,
            'selected_kid_chores': selected_kid_chores,
            'kid_chore_complete_form': kid_chore_complete_form,
            'first_chore_id': first_chore_id,
            'allowance_earned' : allowance_earned
        }


        return render(
            request = request,
            template_name = 'kid.html',
            context = html_data,
        )
        pdb.set_trace()

    def post(self, request, kid_id):
        
        if 'is_complete' in request.POST:
            kid_chore_id = request.POST['chore_number']
            chore_id = request.POST['chore_id']
            kid_chore = Kid_Chore.objects.get(id=kid_chore_id)
            payout = Chore.objects.get(id=chore_id).payout
            kid = Kid.objects.get(id=kid_id)
            kid.allowance_earned += payout
            kid.save()
            kid_chore.is_complete = True
            kid_chore.save()

            
            return redirect(f'/kid/{kid_id}')
        