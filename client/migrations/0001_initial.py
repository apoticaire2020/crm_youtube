# Generated by Django 3.2.4 on 2021-06-14 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, null=True)),
                ('telephone', models.FloatField(max_length=50, null=True)),
                ('date_creation', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
