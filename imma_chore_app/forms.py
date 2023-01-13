from django.forms import ModelForm
from imma_chore_app.models import Parent, Chore, Kid, Kid_Chore

class ParentForm(ModelForm):
    '''used to create or update instances of the Parent Model'''
    class Meta:
        '''includes a single field for the name attribute'''
        model = Parent
        fields = ['name']

class KidForm(ModelForm):
    '''used to create or update instances of the Kid Model'''
    class Meta:
        '''includes a single field for the name attribute'''
        model = Kid
        fields = ['name']
    
class ChoreForm(ModelForm):
    '''used to create or update instances of the Chore Model'''
    class Meta:
        '''includes three fields: name, description and payout attributes'''
        model = Chore
        fields = ['name', 'description', 'payout']

class Kid_ChoreForm(ModelForm):
    '''used to create or update instances of the Kid Chore Model'''
    class Meta:
        '''excludes three attributes of the Kid_Chore Model'''
        model = Kid_Chore
        exclude=('day_of_the_week', 'is_complete', 'kid', 'chore')

class Kid_Chore_CompleteForm(ModelForm):
    '''used to update instances of the Kid_Chore Model'''
    class Meta:
        '''excludes three attributes of the Kid_Chore Model'''
        model = Kid_Chore
       # fields = ['is_complete']
        exclude=('day_of_the_week', 'is_complete', 'kid', 'chore')
