# Generated by Django 3.2.5 on 2022-01-25 22:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20220124_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='commande',
            name='date_ajoutee',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
