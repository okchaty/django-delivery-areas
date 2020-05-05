# Generated by Django 3.0.3 on 2020-05-05 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('area', '0001_initial'),
        ('space', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='areatemplate',
            name='space',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='geo_templates', to='space.Space'),
        ),
    ]
