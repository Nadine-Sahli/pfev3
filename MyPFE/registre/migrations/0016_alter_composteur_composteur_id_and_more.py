# Generated by Django 4.2 on 2023-05-01 15:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('registre', '0015_alter_composteur_composteur_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='composteur',
            name='composteur_id',
            field=models.CharField(default='000', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='composteur',
            name='e_mail',
            field=models.EmailField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='composteur',
            name='nom',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='composteur',
            name='prenom',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='composteur',
            name='pseudo',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='projet',
            name='comp',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='projets', to='registre.composteur'),
        ),
        migrations.AlterField(
            model_name='projet',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='projet',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='projet',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
