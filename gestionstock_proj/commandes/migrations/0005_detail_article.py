# Generated by Django 5.1 on 2024-09-06 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commandes', '0004_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='article',
            field=models.CharField(default='Crayon a bille', max_length=50),
        ),
    ]
