# Generated by Django 2.0b1 on 2017-11-10 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171110_1404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogmodel',
            name='id',
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='blog_id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]