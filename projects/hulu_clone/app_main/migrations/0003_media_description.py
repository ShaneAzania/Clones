# Generated by Django 2.2.4 on 2022-10-02 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0002_auto_20221002_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
