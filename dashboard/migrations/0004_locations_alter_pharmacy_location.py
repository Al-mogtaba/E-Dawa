# Generated by Django 4.0.2 on 2022-03-27 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_medicine'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locations', models.CharField(max_length=300, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.locations'),
        ),
    ]
