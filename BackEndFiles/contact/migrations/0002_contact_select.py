# Generated by Django 4.0.3 on 2022-03-17 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='select',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]