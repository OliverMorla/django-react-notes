# Generated by Django 5.0.1 on 2024-01-17 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=32)),
                ('body', models.TextField(default='')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
