# Generated by Django 5.0.7 on 2024-08-11 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mayurweb', '0010_alter_military_trans_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='military_trans',
            name='img',
            field=models.ImageField(default='https://emifreecar.com/images-new/offcer-coming-soon.jpg', upload_to='services'),
        ),
    ]