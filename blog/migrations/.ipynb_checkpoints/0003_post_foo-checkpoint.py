# Generated by Django 2.0.6 on 2019-05-03 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_text1'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='foo',
            field=models.IntegerField(choices=[(1, 'foo1'), (2, 'foo2')], null=True),
        ),
    ]
