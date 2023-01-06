from django.forms import ModelForm
from imma_chore_app.models import Parent, Chore, Kid

class ParentForm(ModelForm):
    class Meta:
        model = Parent
        fields = ['name']

class KidForm(ModelForm):
    class Meta:
        model = Kid
        fields = ['name', 'parent']# ,['days of week']
    #not sure if all child elements are needed here:
    #########
    #also how are we going to auto populet allowance earned to 0
class ChoreForm(ModelForm):
    class Meta:
        model = Chore
        fields = ['name', 'description', 'payout']