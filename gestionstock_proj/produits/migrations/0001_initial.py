# Generated by Django 5.1 on 2024-09-06 15:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comptes', '0008_local'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('entreprise_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='comptes.entreprise')),
                ('actif', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'fournisseur',
            },
            bases=('comptes.entreprise',),
        ),
    ]
