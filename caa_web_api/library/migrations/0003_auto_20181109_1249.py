# Generated by Django 2.1.2 on 2018-11-09 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20181109_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='book_file',
            field=models.FileField(null=True, upload_to='books/'),
        ),
        migrations.AlterField(
            model_name='library',
            name='cover_image',
            field=models.FileField(null=True, upload_to='cover_images/'),
        ),
    ]