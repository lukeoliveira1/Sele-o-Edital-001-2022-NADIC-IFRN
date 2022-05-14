# Generated by Django 4.0.4 on 2022-05-13 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='candidato',
            fields=[
                ('nomeCompleto', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('dataNascimento', models.DateField()),
                ('endereco', models.CharField(max_length=100)),
            ],
        ),
    ]