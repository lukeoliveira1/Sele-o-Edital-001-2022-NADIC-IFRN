from .models import voto
from django.forms import ModelForm

class votoForm(ModelForm):

    class Meta:
        model = voto
        fields = '__all__'
