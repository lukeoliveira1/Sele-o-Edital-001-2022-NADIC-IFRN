from django.db import models
from candidato.models import candidate
from eleicao.models import election

# Create your models here.
class vote(models.Model):
    cpf = models.CharField(primary_key=True, max_length=20)
    eleicaoPleito = models.ForeignKey(election, on_delete=models.CASCADE)
    candidatoPleito = models.ForeignKey(candidate, on_delete=models.CASCADE)

    def __str__(self):
        return self.cpf + ' - ' + self.eleicaoPleito.nomePleito + " - " + self.candidatoPleito.nomeCompleto