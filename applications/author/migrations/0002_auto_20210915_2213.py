# Generated by Django 3.2.7 on 2021-09-15 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.PositiveIntegerField(default=0, verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=60, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=60, verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='author',
            name='nationality',
            field=models.CharField(max_length=40, verbose_name='Nacionality'),
        ),
    ]