# Generated by Django 2.2 on 2021-02-14 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0004_events_mod'),
    ]

    operations = [
        migrations.CreateModel(
            name='Headline_mod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headlines_name', models.CharField(max_length=50)),
                ('headlines_link', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Headlins',
            },
        ),
    ]