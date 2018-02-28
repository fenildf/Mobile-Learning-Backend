# Generated by Django 2.0.2 on 2018-02-28 05:49

import django.contrib.postgres.fields
from django.db import migrations, models
import question.Questions.QuestionList


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0012_remove_cron_loaded'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_choice_question', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), default=question.Questions.QuestionList.__defaultList__, size=None)),
                ('multiple_choice_question', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), default=question.Questions.QuestionList.__defaultList__, size=None)),
                ('true_or_false_question', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), default=question.Questions.QuestionList.__defaultList__, size=None)),
                ('fill_in_question', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), default=question.Questions.QuestionList.__defaultList__, size=None)),
                ('subjective_question', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), default=question.Questions.QuestionList.__defaultList__, size=None)),
            ],
        ),
    ]
