# Generated by Django 3.0.2 on 2020-03-11 07:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('admin1', '0005_auto_20200309_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_content',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='news_content',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
