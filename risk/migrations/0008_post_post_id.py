# Generated by Django 2.0.6 on 2019-06-24 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk', '0007_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_id',
            field=models.IntegerField(null=True),
        ),
    ]
