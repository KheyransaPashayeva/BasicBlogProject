# Generated by Django 4.0.3 on 2022-03-18 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newblogposts',
            name='update_date',
        ),
        migrations.AddField(
            model_name='newblogposts',
            name='comment_say',
            field=models.CharField(default=1, max_length=100000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newblogposts',
            name='text',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
