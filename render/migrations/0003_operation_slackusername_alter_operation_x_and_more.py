# Generated by Django 4.1.2 on 2022-11-04 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('render', '0002_operation_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='slackUsername',
            field=models.CharField(default='anthonyvictor385', max_length=255),
        ),
        migrations.AlterField(
            model_name='operation',
            name='x',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='operation',
            name='y',
            field=models.IntegerField(default=0),
        ),
    ]
