# Generated by Django 4.0.4 on 2022-06-19 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0010_issue'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='epassword',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),

    ]
