# Generated by Django 4.1.1 on 2022-10-03 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='suporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razao_social', models.CharField(max_length=100)),
                ('nome_fantasia', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=20)),
                ('automacao', models.CharField(max_length=50)),
                ('cod_id', models.CharField(max_length=100)),
                ('nome_contato', models.CharField(max_length=100)),
                ('tel_contato', models.CharField(max_length=100)),
                ('vendedor', models.CharField(max_length=100)),
                ('analista', models.CharField(max_length=100)),
                ('data_instal', models.DateTimeField()),
                ('install', models.BooleanField()),
                ('status', models.CharField(max_length=100)),
                ('obs', models.TextField()),
                ('slug', models.SlugField()),
            ],
        ),
    ]
