# Generated by Django 4.0.1 on 2022-01-29 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0013_alter_topic_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='file',
            field=models.FileField(null=True, upload_to='files'),
        ),
    ]
