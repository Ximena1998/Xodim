# Generated by Django 3.0.8 on 2020-07-13 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sintomatología',
            name='mucosidad',
            field=models.IntegerField(choices=[(1, 'Si'), (0, 'No')]),
        ),
    ]
