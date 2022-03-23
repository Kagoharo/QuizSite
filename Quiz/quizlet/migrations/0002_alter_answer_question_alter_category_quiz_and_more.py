# Generated by Django 4.0.3 on 2022-03-16 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizlet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_answers', to='quizlet.question', default=1, verbose_name='ID вопроса'),
        ),
        migrations.AlterField(
            model_name='category',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_categories', to='quizlet.quiz', default=1, verbose_name='ID опроса'),
        ),
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='quizlet.category', default=1, verbose_name='ID категории'),
        ),
        migrations.AlterField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_questions', to='quizlet.quiz', default=1, verbose_name='ID опроса'),
        ),
    ]
