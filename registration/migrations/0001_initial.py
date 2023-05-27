# Generated by Django 4.2.1 on 2023-05-26 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_name', models.CharField(max_length=200)),
                ('pincode', models.CharField(max_length=6)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('country_code', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(choices=[('model1', 'Model 1'), ('model2', 'Model 2'), ('model3', 'Model 3')], max_length=20)),
                ('manufacturing_date', models.DateTimeField()),
                ('manufacturer', models.CharField(choices=[('manufacturer1', 'Manufacturer 1'), ('manufacturer2', 'Manufacturer 2'), ('manufacturer3', 'Manufacturer 3')], max_length=20)),
                ('color', models.CharField(choices=[('color1', 'Color 1'), ('color2', 'Color 2'), ('color3', 'Color 3')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.address')),
            ],
        ),
    ]
