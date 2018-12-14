# Generated by Django 2.1.2 on 2018-12-13 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PastelUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('student_number', models.CharField(blank=True, max_length=255, null=True)),
                ('fullname', models.CharField(blank=True, max_length=255, null=True)),
                ('date_of_transaction', models.CharField(blank=True, max_length=255, null=True)),
                ('reference_number', models.CharField(blank=True, max_length=255, null=True)),
                ('amount', models.CharField(max_length=255)),
                ('requesting_number', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ['username'],
            },
        ),
    ]
