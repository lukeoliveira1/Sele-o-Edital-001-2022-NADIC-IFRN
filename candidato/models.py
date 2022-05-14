from django.db import models

# Create your models here.
class candidate(models.Model):
    nomeCompleto = models.CharField(max_length=100)
    cpf = models.CharField(primary_key= True, max_length=20)
    dataNascimento = models.DateField()
    endereco = models.CharField(max_length=100)

    def __str__(self):
        return self.nomeCompleto


