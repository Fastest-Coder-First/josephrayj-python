# Generated by Django 4.0.4 on 2023-06-24 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchquery',
            name='weatherTableByDate',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
