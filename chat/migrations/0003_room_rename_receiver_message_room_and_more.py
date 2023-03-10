# Generated by Django 4.0.5 on 2022-12-31 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_rename_room_message_receiver_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.RenameField(
            model_name='message',
            old_name='receiver',
            new_name='room',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='sender',
            new_name='user',
        ),
    ]
