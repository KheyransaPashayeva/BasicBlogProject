# Generated by Django 4.0.3 on 2022-03-17 18:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127)),
                ('email', models.EmailField(max_length=70)),
                ('your_comment', models.TextField()),
                ('date_submitted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
