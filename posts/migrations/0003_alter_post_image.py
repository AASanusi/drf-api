# Generated by Django 3.2.18 on 2023-02-21 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20230221_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='../default_post_xzufhn', upload_to='images/'),
        ),
    ]
