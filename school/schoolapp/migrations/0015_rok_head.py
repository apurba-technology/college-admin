# Generated by Django 2.2 on 2021-02-15 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0014_delete_line'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rok_head',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=50)),
            ],
        ),
    ]
