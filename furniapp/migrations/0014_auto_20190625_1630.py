# Generated by Django 2.1.5 on 2019-06-25 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furniapp', '0013_auto_20190625_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='cw',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='worker',
            name='ex',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='worker',
            name='img',
            field=models.CharField(max_length=500),
        ),
    ]
