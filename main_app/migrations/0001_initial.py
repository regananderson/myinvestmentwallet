# Generated by Django 4.1.7 on 2023-04-26 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('amount', models.IntegerField(default=0)),
                ('description', models.TextField(max_length=250)),
                ('value', models.IntegerField(default=0)),
            ],
        ),
    ]
