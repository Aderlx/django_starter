# Generated by Django 3.1 on 2021-08-13 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avater', models.ImageField(upload_to=None, verbose_name='头像')),
                ('descriotion', models.CharField(max_length=254, verbose_name='描述')),
                ('email', models.EmailField(max_length=254, verbose_name='联系邮箱')),
                ('github', models.URLField(verbose_name='github地址')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profile',
            },
        ),
    ]
