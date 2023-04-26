# Generated by Django 3.2.7 on 2022-11-17 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Feedback', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserPredictDataModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pH', models.CharField(max_length=100)),
                ('Temperature', models.CharField(max_length=100)),
                ('Taste', models.CharField(max_length=100)),
                ('Odour', models.CharField(max_length=100)),
                ('Fat', models.CharField(max_length=100)),
                ('Turbidity', models.CharField(max_length=100)),
                ('Colour', models.CharField(max_length=100)),
                ('Grade', models.CharField(max_length=100)),
            ],
        ),
    ]