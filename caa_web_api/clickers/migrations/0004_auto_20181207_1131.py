# Generated by Django 2.1.2 on 2018-12-07 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clickers', '0003_auto_20181108_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clickermultiplequestions',
            name='courses',
            field=models.CharField(choices=[('accounting', 'accounting'), ('auditing', 'auditing')], default='Please Course', max_length=30),
        ),
    ]