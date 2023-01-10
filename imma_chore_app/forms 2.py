from django.forms import ModelForm
from imma_chore_app.models import Parent, Chore, Kid, Kid_Chore

class ParentForm(ModelForm):
    class Meta:
        model = Parent
        fields = ['name']

class KidForm(ModelForm):
    class Meta:
        model = Kid
        fields = ['name']
    #not sure if all child elements are needed here:
    #########
    #also how are we going to auto populet allowance earned to 0
class ChoreForm(ModelForm):
    class Meta:
        model = Chore
        fields = ['name', 'description', 'payout']
class Kid_ChoreForm(ModelForm):
    class Meta:
        model = Kid_Chore
        exclude=('day_of_the_week', 'is_complete', 'kid', 'chore')