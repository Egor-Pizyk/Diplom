# Generated by Django 4.1.5 on 2023-02-19 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatmessage',
            name='chat',
        ),
        migrations.RemoveField(
            model_name='chatmessage',
            name='user',
        ),
        migrations.DeleteModel(
            name='Chat',
        ),
        migrations.DeleteModel(
            name='ChatMessage',
        ),
    ]
