# Generated by Django 3.2.5 on 2021-08-20 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_message_subject'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['created']},
        ),
    ]
