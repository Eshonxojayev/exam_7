# Generated by Django 5.0.6 on 2024-05-19 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakezone', '0002_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
