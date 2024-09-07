# Generated by Django 5.1 on 2024-09-06 12:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comptes', '0006_vendeur'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='vendeur',
            table='vendeur',
        ),
        migrations.CreateModel(
            name='Contrat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.CharField(max_length=2000)),
                ('dateSignature', models.DateField()),
                ('echeance', models.DateField()),
                ('representant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='comptes.representant')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='comptes.vendeur')),
            ],
            options={
                'db_table': 'contrat',
            },
        ),
    ]
