from django.db import models
from candidato.models import candidate

# Create your models here.
class election(models.Model):
    nomePleito = models.CharField(max_length=50)
    dataInicial = models.DateField()
    dataFinal = models.DateField()
    quantidadeCandidatos = models.IntegerField()
    candidatos =  models.ManyToManyField(candidate)

    def __str__(self):
        return self.nomePleito