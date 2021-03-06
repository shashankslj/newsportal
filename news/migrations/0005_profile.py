# Generated by Django 3.0.2 on 2020-03-20 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0004_news_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.IntegerField(default='0')),
                ('Address', models.CharField(default='', max_length=100)),
                ('proffession', models.CharField(default='', max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('Field_location', models.TextField(default='', max_length=25)),
                ('is_login', models.IntegerField(default='0')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
