# Generated by Django 3.2 on 2022-09-30 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0003_alter_questionanswer_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionanswer',
            name='category',
        ),
    ]
