# Generated by Django 2.1.3 on 2018-11-29 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=40)),
                ('created_at', models.DateTimeField(verbose_name='created at')),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateTimeField(verbose_name='from')),
                ('date_to', models.DateTimeField(verbose_name='to')),
                ('days', models.IntegerField(default=0)),
                ('reason', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=40)),
                ('approved_by', models.CharField(max_length=40)),
                ('created_at', models.DateTimeField(verbose_name='created at')),
                ('updated_at', models.DateTimeField(verbose_name='updated at')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=200)),
                ('client_name', models.CharField(max_length=200)),
                ('remarks', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=40)),
                ('time_line', models.CharField(default='null', max_length=60)),
                ('created_at', models.DateTimeField(verbose_name='created at')),
                ('updated_at', models.DateTimeField(verbose_name='updated at')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=40)),
                ('created_at', models.DateTimeField(verbose_name='created at')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.IntegerField()),
                ('assign_by', models.IntegerField()),
                ('assign_to', models.IntegerField()),
                ('task', models.CharField(max_length=200)),
                ('priority', models.CharField(max_length=40)),
                ('remarks', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=40)),
                ('assign_date', models.DateTimeField(verbose_name='assign_date')),
                ('time_line', models.DateTimeField(verbose_name='time_line')),
                ('created_at', models.DateTimeField(verbose_name='created at')),
                ('updated_at', models.DateTimeField(verbose_name='updated at')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=60)),
                ('passwords', models.CharField(max_length=126)),
                ('contact', models.BigIntegerField(default=0)),
                ('email', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=200)),
                ('join_date', models.DateField(verbose_name='join_date')),
                ('created_at', models.DateTimeField(verbose_name='created at')),
                ('updated_at', models.DateTimeField(verbose_name='updated at')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hrms.Department')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hrms.Role')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='assign_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hrms.User'),
        ),
        migrations.AddField(
            model_name='leave',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hrms.User'),
        ),
    ]
