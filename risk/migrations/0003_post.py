# Generated by Django 2.0.6 on 2019-05-27 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('risk', '0002_auto_20190527_2332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_uid', models.AutoField(primary_key=True, serialize=False)),
                ('post_id', models.IntegerField()),
                ('post_value', models.CharField(max_length=255)),
                ('post_form_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='risk.Field')),
            ],
        ),
    ]
