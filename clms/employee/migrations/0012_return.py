# Generated by Django 4.0.4 on 2022-06-19 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0011_employee_epassword_return'),
    ]

    operations = [
        migrations.CreateModel(
            name='Return',
            fields=[
                ('return_id', models.AutoField(primary_key=True, serialize=False)),
                ('issue_date', models.DateField()),
                ('return_date', models.DateField()),
                ('panalty_status', models.CharField(choices=[('y', 'yes'), ('n', 'no')], max_length=1)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.book')),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.publication')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.students')),
            ],
            options={
                'db_table': 'return_b',
            },
        ),
    ]