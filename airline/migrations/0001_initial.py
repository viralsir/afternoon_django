# Generated by Django 3.2.3 on 2021-06-07 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=35)),
                ('destinations', models.CharField(max_length=35)),
                ('durations', models.IntegerField()),
            ],
        ),
    ]
