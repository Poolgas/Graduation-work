# Generated by Django 5.1.2 on 2024-11-21 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-time_create']},
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['-time_create'], name='post_post_time_cr_623b2b_idx'),
        ),
    ]
