# Generated by Django 3.1.2 on 2020-11-01 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interview_slots', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interviewertimeslot',
            name='candidate',
        ),
    ]
