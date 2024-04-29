# Generated by Django 5.0.3 on 2024-04-17 12:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='homeworks/')),
                ('text', models.TextField(null=True)),
                ('time', models.DateField(auto_now_add=True)),
                ('coin', models.IntegerField(null=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.group')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='User.student')),
            ],
        ),
    ]
