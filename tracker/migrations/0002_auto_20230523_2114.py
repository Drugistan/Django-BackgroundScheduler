# Generated by Django 3.2.18 on 2023-05-23 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='covid',
            name='dateChecked',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='covid',
            name='lastModified',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
