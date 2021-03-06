# Generated by Django 4.0.3 on 2022-03-24 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127)),
                ('author', models.CharField(max_length=170)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('role', models.CharField(max_length=270)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blogposts/')),
                ('text', models.TextField()),
                ('agency', models.IntegerField()),
                ('project_detail', models.TextField()),
            ],
        ),
    ]
