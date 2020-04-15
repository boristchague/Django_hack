# Generated by Django 3.0.5 on 2020-04-15 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('artist_name', models.CharField(max_length=300)),
                ('release_date', models.DateField(auto_now_add=True)),
                ('production_house', models.CharField(max_length=200)),
            ],
        ),
    ]
