# Generated by Django 3.2.7 on 2021-09-23 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_book_category'),
        ('reader', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_loan', to='book.book'),
        ),
    ]
