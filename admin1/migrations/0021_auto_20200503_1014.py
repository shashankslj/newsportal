# Generated by Django 3.0.5 on 2020-05-03 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin1', '0020_auto_20200503_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extended_user',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
