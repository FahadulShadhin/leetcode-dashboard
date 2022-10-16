# Generated by Django 4.1.1 on 2022-10-11 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems_list', '0012_rename_foreign_key_to_difficulty_problem_difficulty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=27, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='problem',
            name='topic',
        ),
        migrations.AddField(
            model_name='problem',
            name='topic',
            field=models.ManyToManyField(to='problems_list.topic'),
        ),
    ]
