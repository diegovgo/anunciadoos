# Generated by Django 2.2.5 on 2020-11-04 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0008_saludinst'),
    ]

    operations = [
        migrations.AddField(
            model_name='saludinst',
            name='url',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
