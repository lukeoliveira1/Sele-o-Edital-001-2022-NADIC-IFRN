from .models import candidate
from django.forms import ModelForm

class candidatoForm(ModelForm):

    class Meta:
        model = candidate
        fields = '__all__'
