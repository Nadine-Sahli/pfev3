# Generated by Django 4.2 on 2023-05-02 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registre', '0016_alter_composteur_composteur_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='NB_GSM',
            new_name='GSM',
        ),
        migrations.RenameField(
            model_name='composteur',
            old_name='NB_GSM',
            new_name='GSM',
        ),
    ]
