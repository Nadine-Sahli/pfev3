# Generated by Django 4.2 on 2023-05-02 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registre', '0025_remove_composteur_nb_gsm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='composteur',
            name='GSM',
        ),
        migrations.AddField(
            model_name='composteur',
            name='NB_GSM',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
