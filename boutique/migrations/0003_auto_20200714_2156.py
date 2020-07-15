# Generated by Django 2.2 on 2020-07-14 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0002_auto_20200714_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=100), max_length=150),
        ),
        migrations.AlterField(
            model_name='produit',
            name='taux_reduction',
            field=models.FloatField(blank=True, default=0),
        ),
    ]