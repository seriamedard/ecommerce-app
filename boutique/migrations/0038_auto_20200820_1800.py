# Generated by Django 2.2 on 2020-08-20 18:00

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0037_produit_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='produit',
            name='picture',
            field=models.URLField(blank=True, default='pass'),
        ),
    ]
