# Generated by Django 2.0.6 on 2019-05-27 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_form_id',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]