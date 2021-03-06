# Generated by Django 3.0.5 on 2020-04-15 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblio', '0003_auto_20200415_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('music_type', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='album',
            name='artist_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblio.Artist'),
        ),
    ]
