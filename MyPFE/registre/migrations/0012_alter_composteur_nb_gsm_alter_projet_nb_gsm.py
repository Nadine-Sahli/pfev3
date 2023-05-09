# Generated by Django 4.2 on 2023-05-01 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registre', '0011_alter_composteur_nb_gsm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='composteur',
            name='NB_GSM',
            field=models.CharField(default='000', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='projet',
            name='NB_GSM',
            field=models.IntegerField(),
        ),
    ]
