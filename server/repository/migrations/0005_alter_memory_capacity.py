# Generated by Django 3.2.5 on 2022-12-06 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0004_alter_memory_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory',
            name='capacity',
            field=models.IntegerField(blank=True, max_length=64, null=True, verbose_name='容量'),
        ),
    ]
