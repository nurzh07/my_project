# Generated by Django 5.1.5 on 2025-03-05 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('seats', models.IntegerField()),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
    ]
