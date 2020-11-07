# Generated by Django 3.1.2 on 2020-11-07 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Compound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PID', models.CharField(max_length=60, unique=True)),
                ('Smiles', models.CharField(db_index=True, max_length=250, unique=True)),
                ('Molecular_Formula', models.CharField(db_index=True, max_length=50)),
                ('Molecular_Weight', models.FloatField()),
                ('H_Bond_Acceptors', models.IntegerField()),
                ('H_Bond_Donors', models.IntegerField()),
                ('Molar_Refractivity', models.FloatField()),
                ('TPSA', models.FloatField()),
                ('ROMol', models.TextField(max_length=150000)),
                ('logP', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('plants', models.ManyToManyField(blank=True, to='main.Plant')),
            ],
        ),
    ]
