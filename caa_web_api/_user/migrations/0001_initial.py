# Generated by Django 2.1.2 on 2018-11-08 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='McUser',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('auth', models.CharField(max_length=20)),
                ('confirmed', models.IntegerField()),
                ('policyagreed', models.IntegerField()),
                ('deleted', models.IntegerField()),
                ('suspended', models.IntegerField()),
                ('mnethostid', models.BigIntegerField()),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=255)),
                ('idnumber', models.CharField(max_length=255)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('emailstop', models.IntegerField()),
                ('icq', models.CharField(max_length=15)),
                ('skype', models.CharField(max_length=50)),
                ('yahoo', models.CharField(max_length=50)),
                ('aim', models.CharField(max_length=50)),
                ('msn', models.CharField(max_length=50)),
                ('phone1', models.CharField(max_length=20)),
                ('phone2', models.CharField(max_length=20)),
                ('institution', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=120)),
                ('country', models.CharField(max_length=2)),
                ('lang', models.CharField(max_length=30)),
                ('calendartype', models.CharField(max_length=30)),
                ('theme', models.CharField(max_length=50)),
                ('timezone', models.CharField(max_length=100)),
                ('firstaccess', models.BigIntegerField()),
                ('lastaccess', models.BigIntegerField()),
                ('lastlogin', models.BigIntegerField()),
                ('currentlogin', models.BigIntegerField()),
                ('lastip', models.CharField(max_length=45)),
                ('secret', models.CharField(max_length=15)),
                ('picture', models.BigIntegerField()),
                ('url', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('descriptionformat', models.IntegerField()),
                ('mailformat', models.IntegerField()),
                ('maildigest', models.IntegerField()),
                ('maildisplay', models.IntegerField()),
                ('autosubscribe', models.IntegerField()),
                ('trackforums', models.IntegerField()),
                ('timecreated', models.BigIntegerField()),
                ('timemodified', models.BigIntegerField()),
                ('trustbitmask', models.BigIntegerField()),
                ('imagealt', models.CharField(blank=True, max_length=255, null=True)),
                ('lastnamephonetic', models.CharField(blank=True, max_length=255, null=True)),
                ('firstnamephonetic', models.CharField(blank=True, max_length=255, null=True)),
                ('middlename', models.CharField(blank=True, max_length=255, null=True)),
                ('alternatename', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'mc_user',
                'managed': False,
            },
        ),
    ]
