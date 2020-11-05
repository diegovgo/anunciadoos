# Generated by Django 2.2.5 on 2020-08-04 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_restaurant_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.AddField(
            model_name='restaurant',
            name='category',
            field=models.ManyToManyField(related_name='restaurant', to='food.Category'),
        ),
    ]
