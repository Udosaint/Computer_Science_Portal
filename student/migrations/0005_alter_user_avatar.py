# Generated by Django 4.1.2 on 2022-11-15 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='user-male.png', null=True, upload_to='avatar/', verbose_name='Profile Picture'),
        ),
    ]
