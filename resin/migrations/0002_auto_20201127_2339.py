# Generated by Django 3.1.1 on 2020-11-28 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculator',
            name='target_resin',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='calculator',
            name='your_resin',
            field=models.PositiveIntegerField(),
        ),
    ]
