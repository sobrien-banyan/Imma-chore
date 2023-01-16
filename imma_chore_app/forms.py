from django.forms import ModelForm
from imma_chore_app.models import Parent, Chore, Kid, Kid_Chore

#form for creation of parent, only name needed
class ParentForm(ModelForm):
    class Meta:
        model = Parent
        fields = ['name']
#form for Kid creation, only name needed at this point, parent FK will be auto added and allownace_earened will be auto populated to 0 upon POST request when creating kid
class KidForm(ModelForm):
    class Meta:
        model = Kid
        fields = ['name']
    
#form creating chore to assign to child  
class ChoreForm(ModelForm):
    class Meta:
        model = Chore
        fields = ['name', 'description', 'payout']

#form is updated to data base when a chore is assigned to a specific chile in the PARENTVIEW
class Kid_ChoreForm(ModelForm):
    class Meta:
        model = Kid_Chore
        exclude=('day_of_the_week', 'is_complete', 'kid', 'chore', 'parent')

