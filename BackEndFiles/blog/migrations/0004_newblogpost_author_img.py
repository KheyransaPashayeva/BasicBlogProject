# Generated by Django 4.0.3 on 2022-03-18 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_newblogposts_newblogpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='newblogpost',
            name='author_img',
            field=models.ImageField(null=True, upload_to='blogposts/'),
        ),
    ]
