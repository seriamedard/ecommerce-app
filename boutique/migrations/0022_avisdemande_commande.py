# Generated by Django 2.2 on 2020-07-29 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0021_contact_adress'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvisDemande',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('prenom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('demande', models.TextField()),
            ],
            options={
                'verbose_name': 'Demande exterieure',
            },
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('contact', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='boutique.Contact')),
                ('panier', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='boutique.Panier')),
                ('produit', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='boutique.Produit')),
            ],
        ),
    ]
