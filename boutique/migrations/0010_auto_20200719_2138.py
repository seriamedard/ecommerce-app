# Generated by Django 2.2 on 2020-07-19 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0009_auto_20200719_1243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=255)),
                ('numero_de_telephone', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='compteuser',
            options={'verbose_name': 'Profil', 'verbose_name_plural': 'Profils'},
        ),
        migrations.AddField(
            model_name='panier',
            name='traite',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='panier',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='utilisateur', to='boutique.CompteUser'),
        ),
    ]
