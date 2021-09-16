# Generated by Django 3.2.7 on 2021-09-15 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '0002_auto_20210915_2213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Title')),
                ('date', models.DateField(verbose_name='Release date')),
                ('book_cover', models.ImageField(upload_to='Image', verbose_name='Book cover')),
                ('visits', models.PositiveIntegerField(verbose_name='Visits')),
                ('authors', models.ManyToManyField(to='author.Author', verbose_name='Autor')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.category', verbose_name='Category')),
            ],
        ),
    ]