# Generated by Django 4.0.3 on 2022-03-17 17:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('about', '0002_delete_newblogposts'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date_submitted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
