# Generated by Django 2.1.2 on 2018-11-09 07:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses_grades', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('book_file', models.FileField(blank=True, null=True, upload_to='book/')),
                ('cover_image', models.FileField(blank=True, null=True, upload_to='cover_images/')),
                ('courses', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses_grades.McCourse')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
