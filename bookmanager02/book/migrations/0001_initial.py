# Generated by Django 5.2.2 on 2025-06-07 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
                ('pub_date', models.DateField(null=True)),
                ('readcount', models.IntegerField(default=0)),
                ('commentcount', models.IntegerField(default=0)),
                ('is_delete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '书籍管理',
                'db_table': 'bookinfo',
            },
        ),
    ]
