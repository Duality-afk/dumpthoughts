# Generated by Django 4.0.5 on 2023-01-01 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_message_userkey'),
    ]

    operations = [
        migrations.CreateModel(
            name='openchat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('senderkey', models.CharField(max_length=100000)),
                ('receiverkey', models.CharField(max_length=100000)),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='receiverkey',
            field=models.CharField(default=0, max_length=100000),
        ),
        migrations.AddField(
            model_name='room',
            name='senderkey',
            field=models.CharField(default=0, max_length=10000000),
        ),
    ]