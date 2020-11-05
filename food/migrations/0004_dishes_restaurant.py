# Generated by Django 2.2.5 on 2020-07-31 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_dishes'),
    ]

    operations = [
        migrations.AddField(
            model_name='dishes',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='food.Restaurant'),
        ),
    ]
