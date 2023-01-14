from django.shortcuts import render, redirect
from django.views import View
import pdb

from django.views import View
from imma_chore_app.forms import ParentForm, KidForm, ChoreForm, Kid_ChoreForm, Kid_Chore_CompleteForm
from imma_chore_app.models import Parent, Kid, Chore, Kid_Chore

# Create your views here.

class HomeView(View):
    def get(self, request):

        html_data = {
            'parent_form' : ParentForm(),
        }

        return render(
            request=request,
            template_name='index.html',
            context= html_data,
        )

    def post(self, request):
        parent_form = ParentForm(request.POST)
        parent = parent_form.save()

        return redirect(f'parent/{parent.id}/1/1')


class ParentView(View):

    parent_object = {}

    def get(self, request, parent_id, kid_id, chore_id):
        # parent = Parent.objects.all()
        # kids = Kid.object.all()
        # kid_form = KidForm()
        kids = Kid.objects.all()
        chores = Chore.objects.all()
        selected_kid_chores = Kid_Chore.objects.all().filter(kid_id=kid_id).select_related('chore')
        # print(selected_kid_chores)
        kid_form = KidForm()
        chore_form = ChoreForm()
        kid_chore_form = Kid_ChoreForm()
        html_data = {
            'kid_list' : kids,
            'kid_form' : kid_form,
            'chore_form' : chore_form,
            'kid_chore_form': kid_chore_form,
            'parent_id' : parent_id,
            'selected_kid' : kid_id,
            'chores' : chores,
            'selected_chore_id': chore_id,
            'selected_kid_chores': selected_kid_chores,
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

    def post(self, request, parent_id, kid_id, chore_id):
        if 'add_child' in request.POST:
            saved_kid = KidForm(request.POST).save()
            saved_kid.parent_id = parent_id
            saved_kid.allowance_earned = 0.0
            saved_kid.save()

            return redirect(f'/parent/{parent_id}/{kid_id}/{chore_id}')

        elif 'create_chore' in request.POST:
            ChoreForm(request.POST).save()

            return redirect(f'/parent/{parent_id}/{kid_id}/{chore_id}')

        elif 'assign_chore' in request.POST:
            saved_kid_chore = Kid_ChoreForm(request.POST).save()
            saved_kid_chore.day_of_the_week = request.POST['day_of_the_week']
            saved_kid_chore.kid_id = kid_id
            saved_kid_chore.chore_id = chore_id
            saved_kid_chore.save()

            return redirect(f'/parent/{parent_id}/{kid_id}/{chore_id}')

        else: 
            return redirect(f'/parent/{parent_id}/{kid_id}/{chore_id}')
        
class KidView(View):


    def get(self, request, kid_id, chore_id):
        kid = Kid.objects.get(id=kid_id)
        kid_money = kid.allowance_earned
        kid_chore_complete_form = Kid_Chore_CompleteForm()

        selected_kid_chores = Kid_Chore.objects.all().filter(kid_id=kid_id).select_related('chore')
        html_data = {
            'kid_id' : kid_id,
            'selected_kid_chores': selected_kid_chores,
            'kid_chore_complete_form': kid_chore_complete_form,
            'first_chore_id': selected_kid_chores[0].id,
            'kid' : kid,
            'kid_money' : kid_money
        }


        return render(
            request = request,
            template_name = 'kid.html',
            context = html_data,
        )

    def post(self, request, kid_id, chore_id):
        #print(request.POST['is_complete'])
        for item in request.POST:
            print(item)
        kid = Kid.objects.get(id=kid_id)
        # kid_chore = Kid_Chore.objects.get(id=chore_id)
        kid_chores = kid.get_chores()
        completed_id = request.POST['button ']
        
        print(kid_chore.payout)
        for chore in kid_chores:
            print(chore)
            if chore.id == completed_id:
                chore.update(is_complete=True)
                kid.allowance += chore.payout

          #adding functionality so that once a chore is done the amount that the chore is worth is addded to the allowance_earned field on that child in the database
        #pdb.set_trace()
        
        kid.chore.set(kid_chore)
        amount_earned = chore.payout
                
        # if kid_chore.is_complete: 
        #     kid_earned_money.allowance_earned += kid_chore.payout
        kid.allowance_earned = request.POST[amount_earned]
        kid.save()

        return redirect(f'/kid/{kid_id}/{kid_chore.id}')
        