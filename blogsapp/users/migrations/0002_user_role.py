# Generated by Django 3.2.15 on 2022-09-30 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Customer'), (2, 'Admin')], default=1),
        ),
    ]
