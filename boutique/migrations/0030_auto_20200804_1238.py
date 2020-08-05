# Generated by Django 2.2 on 2020-08-04 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0029_auto_20200804_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='panieritem',
            name='produits',
        ),
        migrations.AddField(
            model_name='panieritem',
            name='produits',
            field=models.ManyToManyField(blank=True, null=True, related_name='produits', to='boutique.Produit'),
        ),
    ]