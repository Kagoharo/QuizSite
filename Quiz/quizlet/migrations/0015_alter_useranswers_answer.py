# Generated by Django 4.0.3 on 2022-04-14 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizlet', '0014_alter_useranswers_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswers',
            name='answer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_answers', to='quizlet.answer', verbose_name='ID ответа'),
        ),
    ]
