# Generated by Django 3.2.14 on 2022-11-30 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Taller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cleacion', models.DateTimeField(auto_now_add=True)),
                ('titulo', models.CharField(max_length=150)),
                ('descripcion', models.TextField()),
                ('ponente', models.CharField(max_length=180)),
                ('lugar', models.CharField(max_length=200)),
            ],
        ),
    ]
