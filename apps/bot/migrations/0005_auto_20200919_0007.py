# Generated by Django 2.2.13 on 2020-09-19 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_auto_20200919_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='inserted_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]