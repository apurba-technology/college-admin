# Generated by Django 2.2 on 2021-02-15 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0015_rok_head'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rok_head',
            name='link',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='rok_head',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
