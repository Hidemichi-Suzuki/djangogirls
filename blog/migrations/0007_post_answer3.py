# Generated by Django 2.0.6 on 2019-05-16 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190503_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='answer3',
            field=models.TextField(null=True),
        ),
    ]
