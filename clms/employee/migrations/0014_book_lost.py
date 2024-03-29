# Generated by Django 4.0.6 on 2022-08-09 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0013_penalty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_lost',
            fields=[
                ('book_lost_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.book')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.students')),
            ],
            options={
                'db_table': 'book_lost',
            },
        ),
    ]
