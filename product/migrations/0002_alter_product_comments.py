# Generated by Django 5.0.6 on 2024-05-19 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='comments',
            field=models.ManyToManyField(blank=True, to='product.comment'),
        ),
    ]
