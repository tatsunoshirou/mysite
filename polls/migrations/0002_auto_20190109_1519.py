# Generated by Django 2.1.4 on 2019-01-09 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.TextField(max_length=145, verbose_name='メッセージ'),
        ),
    ]
