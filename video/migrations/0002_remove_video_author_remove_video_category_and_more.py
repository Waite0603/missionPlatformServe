# Generated by Django 4.2.13 on 2024-09-14 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='author',
        ),
        migrations.RemoveField(
            model_name='video',
            name='category',
        ),
        migrations.AddField(
            model_name='uploadrecord',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='uploadrecord',
            name='path',
            field=models.FilePathField(max_length=255, path='upload/video'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]
