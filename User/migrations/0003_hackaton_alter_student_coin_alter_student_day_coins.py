# Generated by Django 5.0.3 on 2024-04-24 13:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_homework'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hackaton',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(choices=[('Backend', 'Backend'), ('Frontend', 'Frontend'), ('Designer', 'Designer')], max_length=200)),
                ('date', models.DateField(auto_now=True)),
                ('coin', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='coin',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='day',
            field=models.CharField(max_length=200),
        ),
        migrations.CreateModel(
            name='Coins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coins', models.IntegerField(choices=[('-2', '-2'), ('1', '1'), ('3', '3'), ('5', '5'), ('10', '10')])),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.student')),
            ],
        ),
    ]
