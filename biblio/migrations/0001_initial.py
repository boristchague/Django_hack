# Generated by Django 3.0.5 on 2020-04-14 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Aucune musique', max_length=220)),
                ('duration', models.IntegerField(default=0, help_text='Durée en séconde')),
                ('album', models.CharField(max_length=200)),
                ('lyrics', models.TextField(blank=True)),
            ],
        ),
    ]
