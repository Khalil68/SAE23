# Generated by Django 4.0.5 on 2022-06-08 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cat_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('descriptif', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_client', models.BigIntegerField(null=True)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('date_inscription', models.DateField()),
                ('adresse', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='commandes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_commande', models.BigIntegerField(null=True)),
                ('client', models.CharField(max_length=100)),
                ('date_inscription', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('photo', models.FileField(upload_to='')),
                ('marques', models.CharField(max_length=100)),
                ('auteur', models.CharField(max_length=100)),
                ('categorie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='drive.cat_product')),
            ],
        ),
    ]