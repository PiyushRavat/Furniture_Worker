# Generated by Django 2.1.5 on 2019-06-25 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furniapp', '0017_auto_20190625_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='slug',
            field=models.SlugField(default=5, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='worker',
            name='img',
            field=models.CharField(max_length=500),
        ),
    ]
