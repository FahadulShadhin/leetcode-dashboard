# Generated by Django 4.1.1 on 2022-09-16 11:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('problems_list', '0002_problem_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=55, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='problem',
            name='topic',
        ),
        migrations.AddField(
            model_name='problem',
            name='topics',
            field=models.ManyToManyField(to='problems_list.topic'),
        ),
    ]
