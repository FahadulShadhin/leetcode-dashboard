# Generated by Django 4.1.1 on 2022-10-19 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems_list', '0016_rename_github_links_url_remove_links_leetcode_github_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='mote_img',
            field=models.ImageField(default=None, null=True, upload_to='img/'),
        ),
    ]
