# Generated by Django 4.1.2 on 2022-11-16 08:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_level_school_session_semester'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50, null=True)),
                ('app_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.school_session')),
            ],
        ),
    ]