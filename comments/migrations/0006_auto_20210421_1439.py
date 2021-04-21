# Generated by Django 3.1.7 on 2021-04-21 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0005_auto_20210421_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.SmallIntegerField(choices=[(1, 'Terrible'), (2, 'Malo'), (3, 'Regular'), (4, 'Bueno'), (5, 'Excelente')]),
        ),
    ]
