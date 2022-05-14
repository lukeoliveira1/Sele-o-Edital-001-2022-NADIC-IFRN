from .models import election
from django.forms import ModelForm

class eleicaoForm(ModelForm):

    class Meta:
        model = election
        fields = '__all__'
