# Generated by Django 2.2.5 on 2021-02-22 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0028_auto_20210211_0235'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='url',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
