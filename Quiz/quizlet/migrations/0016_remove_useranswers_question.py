# Generated by Django 4.0.3 on 2022-04-14 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizlet', '0015_alter_useranswers_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useranswers',
            name='question',
        ),
    ]