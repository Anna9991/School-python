# Generated by Django 5.1.1 on 2024-09-09 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_alter_teacher_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foundation_year', models.IntegerField()),
                ('number_of_students', models.IntegerField(default=0)),
                ('number_of_awards', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('facebook_url', models.URLField()),
                ('instagram_url', models.URLField()),
                ('youtube_url', models.URLField()),
            ],
        ),
    ]
