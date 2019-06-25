# Generated by Django 2.1.5 on 2019-06-25 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furniapp', '0019_auto_20190625_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='category',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='cw',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='ex',
        ),
        migrations.AddField(
            model_name='worker',
            name='desc',
            field=models.CharField(default=5, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='worker',
            name='img',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='name',
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name='worker',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
    ]
