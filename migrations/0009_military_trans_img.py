# Generated by Django 5.0.7 on 2024-08-09 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mayurweb', '0008_service_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='military_trans',
            name='img',
            field=models.ImageField(default='image', upload_to='services'),
        ),
    ]
