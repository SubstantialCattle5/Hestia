# Generated by Django 4.0.4 on 2022-07-10 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_questions_title_alter_questions_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='id',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='user',
        ),
        migrations.AlterField(
            model_name='questions',
            name='address',
            field=models.TextField(default='', primary_key=True, serialize=False),
        ),
    ]
