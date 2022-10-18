# Generated by Django 4.1.1 on 2022-10-13 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems_list', '0015_links_alter_problem_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='links',
            old_name='github',
            new_name='url',
        ),
        migrations.RemoveField(
            model_name='links',
            name='leetcode_github',
        ),
        migrations.RemoveField(
            model_name='links',
            name='linked_in',
        ),
        migrations.RemoveField(
            model_name='links',
            name='medium',
        ),
        migrations.AddField(
            model_name='links',
            name='name',
            field=models.CharField(max_length=256, null=True),
        ),
    ]