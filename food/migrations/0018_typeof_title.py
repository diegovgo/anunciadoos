# Generated by Django 2.2.5 on 2021-01-19 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0017_remove_dishes_restaurant'),
    ]

    operations = [
        migrations.AddField(
            model_name='typeof',
            name='title',
            field=models.CharField(default=models.CharField(max_length=64), max_length=64),
        ),
    ]