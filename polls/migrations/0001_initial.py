# Generated by Django 2.1.4 on 2019-01-09 02:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='名前')),
                ('message', models.TextField(max_length=140, verbose_name='メッセージ')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': '投稿',
                'verbose_name_plural': '投稿',
                'db_table': 'post',
            },
        ),
    ]
