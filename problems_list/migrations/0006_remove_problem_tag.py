# Generated by Django 4.1.1 on 2022-10-07 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems_list', '0005_problem_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='tag',
        ),
    ]
