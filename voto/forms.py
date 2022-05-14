from .models import vote
from django.forms import ModelForm

class votoForm(ModelForm):

    class Meta:
        model = vote
        fields = '__all__'
