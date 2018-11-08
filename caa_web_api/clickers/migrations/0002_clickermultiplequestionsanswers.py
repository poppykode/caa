# Generated by Django 2.1.2 on 2018-11-08 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clickers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClickerMultipleQuestionsAnswers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('couser_id', models.CharField(max_length=255)),
                ('answer', models.CharField(max_length=255)),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clickers.ClickerMultipleQuestions')),
            ],
        ),
    ]
