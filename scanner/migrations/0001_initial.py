# Generated by Django 4.2 on 2024-11-10 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScannnedData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
