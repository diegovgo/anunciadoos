# Generated by Django 2.2.5 on 2021-01-18 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0013_auto_20210118_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dishes',
            name='restaurant',
        ),
        migrations.AddField(
            model_name='typeof',
            name='restaurante',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='typeof', to='food.Restaurant'),
        ),
    ]
